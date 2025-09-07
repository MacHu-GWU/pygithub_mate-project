# -*- coding: utf-8 -*-

from pygithub_mate.repo import BaseGitHubRepo
from settings import settings

repo = BaseGitHubRepo(
    owner_name=settings.owner_name,
    repo_name=settings.repo_name,
    github_kwargs=dict(login_or_token=settings.token),
)

tag_name = "v1"
release_name = "v1"
# repo.create_tag_on_latest_commit_on_default_branch(tag_name)

# commit_sha = repo.get_latest_commit_sha_on_default_branch()
# --- Commands
# fmt: off
# repo.put_tag_on_commit(commit_sha=commit_sha, tag_name=tag_name)
# repo.put_release(commit_sha=commit_sha, tag_name=tag_name, release_name=release_name)
# repo.put_tag_on_latest_commit_on_default_branch(tag_name=tag_name)
# repo.put_release_on_latest_commit_on_default_branch(tag_name=tag_name, release_name=release_name)
# fmt: off