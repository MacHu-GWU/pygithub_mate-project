# -*- coding: utf-8 -*-

from pygithub_mate.repo import BaseGitHubRepo
from settings import settings

repo = BaseGitHubRepo(
    owner_name=settings.owner_name,
    repo_name=settings.repo_name,
    github_kwargs=dict(login_or_token=settings.token),
)

# fmt: off

# === Test 1
# tag_name = "v1"
# release_name = "v1"
# commit_sha = repo.get_latest_commit_sha_on_default_branch()
# --- Test 1-1
# repo.put_release(commit_sha=commit_sha, tag_name=tag_name, release_name=release_name)
# --- Test 1-2
# repo.put_release_on_latest_commit_on_default_branch(tag_name=tag_name, release_name=release_name)
# fmt: on

# === Test 2
tag_name = "release-v1"
release_name = "release-v1"
branch_name = "release"
# --- Test 2-1
repo.put_release_on_latest_commit_on_branch(branch_name=branch_name, tag_name=tag_name, release_name=release_name)
# --- Test 2-2
# repo.delete_release(release_name=release_name)
# repo.delete_tag(tag_name=tag_name)
