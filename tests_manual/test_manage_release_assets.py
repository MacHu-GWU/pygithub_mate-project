# -*- coding: utf-8 -*-

from pygithub_mate.repo import BaseGitHubRepo
from pathlib import Path
from settings import settings

repo = BaseGitHubRepo(
    owner_name=settings.owner_name,
    repo_name=settings.repo_name,
    github_kwargs=dict(login_or_token=settings.token),
)

release_name = "v1"
release = repo.get_git_release(release_name)
path_to_name_mapping = {
    Path(__file__): Path(__file__).name,
}
# fmt: off
# --- Test 1
repo.put_assets_to_release(release=release, path_to_name_mapping=path_to_name_mapping)
# fmt: off
