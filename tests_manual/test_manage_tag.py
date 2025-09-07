# -*- coding: utf-8 -*-

from pygithub_mate.repo import BaseGitHubRepo
from settings import settings

repo = BaseGitHubRepo(
    owner_name=settings.owner_name,
    repo_name=settings.repo_name,
    github_kwargs=dict(login_or_token=settings.token),
)

# === Test 1
# tag_name = "v1"
# --- Test 1-1
# repo.create_tag_on_latest_commit_on_default_branch(tag_name)
# --- Test 1-2
# commit_sha = repo.get_latest_commit_sha_on_default_branch()
# repo.put_tag_on_commit(commit_sha=commit_sha, tag_name=tag_name)
# --- Test 1-3
# repo.put_tag_on_latest_commit_on_default_branch(tag_name=tag_name)

# === Test 2
tag_name = "dev-v1"
branch_name = "dev"
# --- Test 2-1
repo.put_tag_on_latest_commit_on_branch(branch_name=branch_name, tag_name=tag_name)
# --- Test 2-2
# repo.delete_tag(tag_name)
