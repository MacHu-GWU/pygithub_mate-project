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
commit_sha = repo.get_latest_commit_sha_on_default_branch()

# fmt: off
# --- Test 1
repo.put_release(commit_sha=commit_sha, tag_name=tag_name, release_name=release_name)

# --- Test 2
# repo.put_release_on_latest_commit_on_default_branch(tag_name=tag_name, release_name=release_name)
# fmt: off
