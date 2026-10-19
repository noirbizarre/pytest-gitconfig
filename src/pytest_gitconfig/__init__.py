from __future__ import annotations

from pathlib import Path

from .plugin import (
    DEFAULT_GIT_BRANCH as DEFAULT_GIT_BRANCH,
    DEFAULT_GIT_USER_EMAIL as DEFAULT_GIT_USER_EMAIL,
    DEFAULT_GIT_USER_NAME as DEFAULT_GIT_USER_NAME,
    UNSET as UNSET,
    GitConfig as GitConfig,
)

_version_file = Path(__file__).parent / "VERSION"
__version__ = _version_file.read_text() if _version_file.is_file() else "0.0.0.dev"
