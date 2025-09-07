# -*- coding: utf-8 -*-

from pygithub_mate import api


def test():
    _ = api

    _ = api.Emoji

    _ = api.BaseLogger
    _ = api.BaseLogger.info
    _ = api.BaseLogger.shorten_sha

    _ = api.BaseGitHubApiRunner
    _ = api.BaseGitHubApiRunner.gh

    _ = api.TagAndRef
    _ = api.TagAndRef.exists

    _ = api.ReleaseAndTagAndRef
    _ = api.ReleaseAndTagAndRef.exists

    _ = api.IsTagLatestOnDefaultBranchResult

    _ = api.BaseGitHubRepo
    _ = api.BaseGitHubRepo.repo_full_name
    _ = api.BaseGitHubRepo.repo
    _ = api.BaseGitHubRepo.repo_default_branch_name
    _ = api.BaseGitHubRepo.get_latest_commit_sha_on_branch
    _ = api.BaseGitHubRepo.get_latest_commit_sha_on_default_branch
    _ = api.BaseGitHubRepo.latest_commit_sha_on_default_branch
    _ = api.BaseGitHubRepo.get_git_tag_and_ref
    _ = api.BaseGitHubRepo.is_tag_latest_on_default_branch
    _ = api.BaseGitHubRepo.delete_tag
    _ = api.BaseGitHubRepo.create_tag_on_commit
    _ = api.BaseGitHubRepo.create_tag_on_latest_commit_on_default_branch
    _ = api.BaseGitHubRepo.get_git_release
    _ = api.BaseGitHubRepo.put_tag_on_commit
    _ = api.BaseGitHubRepo.put_tag_on_latest_commit_on_default_branch
    _ = api.BaseGitHubRepo.delete_release
    _ = api.BaseGitHubRepo.create_release
    _ = api.BaseGitHubRepo.put_release
    _ = api.BaseGitHubRepo.put_release_on_latest_commit_on_default_branch
    _ = api.BaseGitHubRepo.put_assets_to_release


if __name__ == "__main__":
    from pygithub_mate.tests import run_cov_test

    run_cov_test(
        __file__,
        "pygithub_mate.api",
        preview=False,
    )
