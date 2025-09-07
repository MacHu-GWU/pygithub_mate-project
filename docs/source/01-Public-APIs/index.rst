Public APIs
==============================================================================
Import ``pygithub_mate``::

    import pygithub_mate.api as pygithub_mate

**Core Classes:**

- :class:`BaseLogger <pygithub_mate.base.BaseLogger>`: Base logging functionality with configurable output control.
- :class:`BaseGitHubApiRunner <pygithub_mate.base.BaseGitHubApiRunner>`: Base class for GitHub API operations with authentication and logging.
- :class:`BaseGitHubRepo <pygithub_mate.repo.BaseGitHubRepo>`: Main class for GitHub repository operations.

**Data Containers:**

- :class:`TagAndRef <pygithub_mate.base.TagAndRef>`: Container for Git tag and reference objects.
- :class:`ReleaseAndTagAndRef <pygithub_mate.base.ReleaseAndTagAndRef>`: Container for GitHub release, tag, and reference objects.
- :class:`IsTagLatestOnDefaultBranchResult <pygithub_mate.repo.IsTagLatestOnDefaultBranchResult>`: Result container for tag currency checks.

**Repository Information:**

- :attr:`BaseGitHubRepo.repo_full_name <pygithub_mate.repo.BaseGitHubRepo.repo_full_name>`: Full repository name in owner/repo format.
- :attr:`BaseGitHubRepo.repo <pygithub_mate.repo.BaseGitHubRepo.repo>`: GitHub repository object.
- :attr:`BaseGitHubRepo.repo_default_branch_name <pygithub_mate.repo.BaseGitHubRepo.repo_default_branch_name>`: Default branch name.

**Commit Operations:**

- :meth:`BaseGitHubRepo.get_latest_commit_sha_on_branch <pygithub_mate.repo.BaseGitHubRepo.get_latest_commit_sha_on_branch>`: Get latest commit SHA on specified branch.
- :meth:`BaseGitHubRepo.get_latest_commit_sha_on_default_branch <pygithub_mate.repo.BaseGitHubRepo.get_latest_commit_sha_on_default_branch>`: Get latest commit SHA on default branch.
- :attr:`BaseGitHubRepo.latest_commit_sha_on_default_branch <pygithub_mate.repo.BaseGitHubRepo.latest_commit_sha_on_default_branch>`: Cached latest commit SHA on default branch.

**Tag Operations:**

- :meth:`BaseGitHubRepo.get_git_tag_and_ref <pygithub_mate.repo.BaseGitHubRepo.get_git_tag_and_ref>`: Retrieve Git tag and reference objects.
- :meth:`BaseGitHubRepo.is_tag_latest_on_default_branch <pygithub_mate.repo.BaseGitHubRepo.is_tag_latest_on_default_branch>`: Check if tag points to latest commit on default branch.
- :meth:`BaseGitHubRepo.delete_tag <pygithub_mate.repo.BaseGitHubRepo.delete_tag>`: Delete existing Git tag reference.
- :meth:`BaseGitHubRepo.create_tag_on_commit <pygithub_mate.repo.BaseGitHubRepo.create_tag_on_commit>`: Create new Git tag on specific commit.
- :meth:`BaseGitHubRepo.create_tag_on_latest_commit_on_default_branch <pygithub_mate.repo.BaseGitHubRepo.create_tag_on_latest_commit_on_default_branch>`: Create new Git tag on latest commit of default branch.
- :meth:`BaseGitHubRepo.put_tag_on_commit <pygithub_mate.repo.BaseGitHubRepo.put_tag_on_commit>`: Ensure Git tag points to specific commit with intelligent workflow.
- :meth:`BaseGitHubRepo.put_tag_on_latest_commit_on_branch <pygithub_mate.repo.BaseGitHubRepo.put_tag_on_latest_commit_on_branch>`: Ensure Git tag points to latest commit on specified branch.
- :meth:`BaseGitHubRepo.put_tag_on_latest_commit_on_default_branch <pygithub_mate.repo.BaseGitHubRepo.put_tag_on_latest_commit_on_default_branch>`: Ensure Git tag points to latest commit on default branch.

**Release Operations:**

- :meth:`BaseGitHubRepo.get_git_release <pygithub_mate.repo.BaseGitHubRepo.get_git_release>`: Retrieve GitHub release object.
- :meth:`BaseGitHubRepo.delete_release <pygithub_mate.repo.BaseGitHubRepo.delete_release>`: Delete existing GitHub release.
- :meth:`BaseGitHubRepo.create_release <pygithub_mate.repo.BaseGitHubRepo.create_release>`: Create new GitHub release.
- :meth:`BaseGitHubRepo.put_release <pygithub_mate.repo.BaseGitHubRepo.put_release>`: Ensure GitHub release and tag point to specific commit with comprehensive workflow.
- :meth:`BaseGitHubRepo.put_release_on_latest_commit_on_branch <pygithub_mate.repo.BaseGitHubRepo.put_release_on_latest_commit_on_branch>`: Ensure GitHub release and tag point to latest commit on specified branch.
- :meth:`BaseGitHubRepo.put_release_on_latest_commit_on_default_branch <pygithub_mate.repo.BaseGitHubRepo.put_release_on_latest_commit_on_default_branch>`: Ensure GitHub release and tag point to latest commit on default branch.
- :meth:`BaseGitHubRepo.put_assets_to_release <pygithub_mate.repo.BaseGitHubRepo.put_assets_to_release>`: Upload assets to release with intelligent duplicate handling.

**Utilities:**

- :class:`Emoji <pygithub_mate.emoji.Emoji>`: Emoji constants for logging and display.
- :meth:`BaseLogger.info <pygithub_mate.base.BaseLogger.info>`: Log informational messages with verbosity control.
- :meth:`BaseLogger.shorten_sha <pygithub_mate.base.BaseLogger.shorten_sha>`: Shorten Git SHA for display purposes.