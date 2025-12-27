from __future__ import annotations

from pytest_gitconfig import GitConfig
from pytest_gitconfig.plugin import DEFAULT_GIT_BRANCH, DEFAULT_GIT_USER_EMAIL, DEFAULT_GIT_USER_NAME

USER_NAME = "Overridden user Name"
USER_EMAIL = "hello@nowhere.com"
DEFAULT_BRANCH = "any_branch"


# Session-scoped default are already overridden by conftest.py


def test_session_fixtures_override_session_scoped_defaults(
    default_gitconfig: GitConfig,
    default_git_user_name: str,
    default_git_user_email: str,
    default_git_init_default_branch: str,
):
    assert default_gitconfig.get("user.name") == default_git_user_name
    assert default_gitconfig.get("user.email") == default_git_user_email
    assert default_gitconfig.get("init.defaultBranch") == default_git_init_default_branch
    assert default_git_user_name != DEFAULT_GIT_USER_NAME
    assert default_git_user_email != DEFAULT_GIT_USER_EMAIL
    assert default_git_init_default_branch != DEFAULT_GIT_BRANCH


def test_session_fixtures_override_function_scoped_defaults(
    gitconfig: GitConfig,
    git_user_name: str,
    git_user_email: str,
    git_init_default_branch: str,
    default_git_user_name: str,
    default_git_user_email: str,
    default_git_init_default_branch: str,
):
    assert gitconfig.get("user.name") == default_git_user_name
    assert gitconfig.get("user.email") == default_git_user_email
    assert gitconfig.get("init.defaultBranch") == default_git_init_default_branch
    assert git_user_name == default_git_user_name
    assert git_user_email == default_git_user_email
    assert git_init_default_branch == default_git_init_default_branch
