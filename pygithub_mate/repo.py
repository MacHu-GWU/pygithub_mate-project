# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

from func_args.api import BaseFrozenModel, REQ
from github import Github, GithubException

from .typehint import T_PRINTER
from .base import (
    BaseGitHubApiRunner,
    TagAndRef,
)

if T.TYPE_CHECKING:
    from github.Repository import Repository
    from github.GitRef import GitRef
    from github.GitTag import GitTag
    from github.GitRelease import GitRelease


@dataclasses.dataclass(frozen=True)
class IsTagLatestOnMainResult:
    """
    A container for the result of checking if a tag is the latest on the main branch.

    :param is_latest: True if the tag points to the latest commit on the default branch
    :param latest_commit_sha: SHA of the latest commit on the default branch
    :param tag_and_ref: The Git tag and reference objects for the tag
    """

    is_latest: bool = dataclasses.field()
    latest_commit_sha: str = dataclasses.field()
    tag_and_ref: "TagAndRef" = dataclasses.field()


@dataclasses.dataclass(frozen=True)
class BaseGitHubRepo(BaseGitHubApiRunner):
    """
    GitHub repository operations.

    Provides comprehensive repository management functionality including
    tag creation, deletion, branch operations, and commit tracking.
    Follows the command pattern with repository details stored as
    attributes and dynamic operations as method parameters.

    :param owner_name: GitHub repository owner/organization name
    :param repo_name: Repository name
    """
    owner_name: str = dataclasses.field(default=REQ)
    repo_name: str = dataclasses.field(default=REQ)

    @cached_property
    def repo_full_name(self) -> str:
        """
        Full name of the repository in the format "owner/repo".
        """
        return f"{self.owner_name}/{self.repo_name}"

    @cached_property
    def repo(self) -> "Repository":
        """
        GitHub repository object.
        """
        return self.gh.get_repo(self.repo_full_name)

    @cached_property
    def repo_default_branch_name(self) -> str:
        """
        Default branch name of the repository.
        """
        return self.repo.default_branch

    def get_latest_commit_sha_on_branch(
        self,
        branch_name: str,
    ) -> str:
        """
        Get the SHA of the latest commit on a specific branch.

        :param branch_name: Name of the branch to query

        :returns: SHA hash of the latest commit on the branch
        """
        return self.repo.get_branch(branch_name).commit.sha

    def get_latest_commit_sha_on_default_branch(self) -> str:
        """
        Get the SHA of the latest commit on the repository's default branch.

        :returns: SHA hash of the latest commit on the default branch
        """
        return self.get_latest_commit_sha_on_branch(
            branch_name=self.repo_default_branch_name,
        )

    @cached_property
    def latest_commit_sha_on_default_branch(self) -> str:
        """
        SHA of the latest commit on the repository's default branch.
        """
        return self.get_latest_commit_sha_on_default_branch()

    def get_git_tag_and_ref(
        self,
        tag_name: str,
    ) -> "TagAndRef":
        """
        Retrieve the Git tag and reference objects for the specified tag.

        Attempts to fetch both the Git tag object and the Git reference for the
        specified tag name. Handles cases where the tag or reference doesn't exist.

        :param tag_name: Name of the tag to retrieve

        :returns: TagAndRef object containing:
            - tag=None, ref=None if the tag reference doesn't exist
            - tag=None, ref=GitRef if the reference exists but the tag object doesn't
            - tag=GitTag, ref=GitRef if both exist

        :raises GithubException: For API errors other than 404 (not found)
        """
        # Try to get the tag reference first
        try:
            ref = self.repo.get_git_ref(f"tags/{tag_name}")
        except GithubException as e:
            if e.status == 404:
                return TagAndRef()  # Tag reference doesn't exist
            else:  # pragma: no cover
                raise e
        except Exception:
            raise

        # Get the SHA that the tag reference points to
        tag_sha = ref.object.sha

        # Try to get the actual tag object
        try:
            tag = self.repo.get_git_tag(tag_sha)
        except GithubException as e:
            if e.status == 404:
                # Reference exists but tag object doesn't
                return TagAndRef(tag=None, ref=ref)
            else:  # pragma: no cover
                raise
        except Exception:
            raise

        return TagAndRef(tag=tag, ref=ref)

    def is_tag_latest_on_main(
        self,
        tag_name: str,
    ) -> "IsTagLatestOnMainResult":
        """
        Check if the specified tag points to the latest commit on the default branch.

        Compares the commit SHA that the tag points to with the SHA of the latest
        commit on the default branch to determine if the tag is up-to-date.

        :param tag_name: Name of the tag to check

        :returns: IsTagLatestOnMainResult object containing:
            - is_latest: True if tag is latest, False otherwise (or if tag doesn't exist)
            - latest_commit_sha: SHA of the latest commit on the default branch
            - tag_and_ref: TagAndRef object containing the Git tag and reference

        Note:
            If the tag doesn't exist, is_latest will be False.
        """
        latest_commit_sha = self.get_latest_commit_sha_on_default_branch()
        tag_and_ref = self.get_git_tag_and_ref(tag_name)

        if tag_and_ref.tag is None:
            # Tag doesn't exist, so it can't be latest
            flag = False
        else:
            # Compare tag's commit SHA with latest commit SHA
            flag = tag_and_ref.tag.object.sha == latest_commit_sha
        return IsTagLatestOnMainResult(
            is_latest=flag,
            latest_commit_sha=latest_commit_sha,
            tag_and_ref=tag_and_ref,
        )

    def delete_tag(
        self,
        tag_name: str,
    ) -> bool:
        """
        Delete the existing Git tag reference if it exists.

        Attempts to find and delete the Git tag reference for the specified tag name.
        This removes the tag from the repository, making it available for recreation.

        :param tag_name: Name of the tag to delete

        :returns: True if a tag was found and deleted, False if no tag existed

        :raises GithubException: If the deletion fails due to API errors other than 404
        """
        try:
            # Get the tag reference
            ref = self.repo.get_git_ref(f"tags/{tag_name}")
            ref.delete()  # Delete the tag reference
            return True
        except GithubException as e:
            if e.status == 404:
                return False  # Tag doesn't exist, nothing to delete
            else:  # pragma: no cover
                raise e

    def create_tag_on_latest_commit_on_default_branch(
        self,
        tag_name: str,
        tag_message: str | None = None,
    ) -> "TagAndRef":
        """
        Create a new Git tag and reference pointing to the latest commit on default branch.

        Creates both a Git tag object and a Git reference for the specified tag name.
        Always uses the latest commit from the default branch.

        :param tag_name: Name for the new Git tag
        :param tag_message: Optional message for the tag (defaults to "Tag {tag_name}")

        :returns: TagAndRef object containing the created Git tag and reference

        :raises GithubException: If tag creation fails (e.g., tag already exists)
        """
        # Use latest commit if none specified
        latest_commit_sha = self.latest_commit_sha_on_default_branch
        if tag_message is None:
            tag_message = f"Tag {tag_name}"
        # Create the Git tag object
        tag = self.repo.create_git_tag(
            tag=tag_name,
            message=tag_message,
            object=latest_commit_sha,
            type="commit",
        )

        # Create the Git reference pointing to the tag
        ref = self.repo.create_git_ref(
            ref=f"refs/tags/{tag_name}",
            sha=tag.sha,
        )
        return TagAndRef(tag=tag, ref=ref)
