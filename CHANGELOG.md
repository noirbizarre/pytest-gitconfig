# Changelog

## 🚀 0.9.0 (2025-12-28)

### 💫 New features

- **gitconfig**: added `delete(key)` method
- **gitconfig**: allow using `.set(key, value)` form
- **set**: add `set_default_gitconfig` and `set_config` to set multiple settings at once

### 🐛 Bug fixes

- **fixtures**: ensure function-scoped fixtures inherit the session-scoped fixtures values
- restore the default_gitconfig autouse but trick pytest to have `git_env_var` set before (for testing purpose)

### 📖 Documentation

- **gitconfig**: added some docstrings to the public methods
- **README**: fix the example fixture scope

### 📦 Build

- **tox**: drop `tox-pdm` and rely on `dependency-groups`
- use uv as dependency resolver

### 🧹 Chores

- hide some traceback to clean stacktraces


## 🚀 0.8.0 (2025-10-12)

### 🚨 Breaking changes

- update the stack, drop support for Python 3.8 and 3.9, add support for Python 3.13 and 3.14 ([#17](https://github.com/noirbizarre/pytest-gitconfig/issues/17))

### 📦 Build

- **pyproject**: use PEP 639 `license` and `license-file` (fix [#15](https://github.com/noirbizarre/pytest-gitconfig/issues/15))


## 🚀 0.7.0 (2024-08-11)

### 💫 New features

- add support for unsetting config values via override fixtures

### 🐛 Bug fixes

- **typing**: expose `UNSET` type at root leel

### 📖 Documentation

- fix typos and enhance

### 📦 Build

- update the build stack


## 🚀 0.6.0 (2023-10-15)

### 💫 New features

- add a `GitConfig.override()` context manager setting values
- support a 2nd `get()` parameter as default value if the key is not found in git config

### 📖 Documentation

- **README**: improve README documentation until we have a decent RTFD ref documentation

## 🚀 0.5.0 (2023-10-14)

### 💫 New features

- **set**: handle dict with dotted keys as `GitConfig.set()` parameter

### 📖 Documentation

- **README**: improve `gitconfig.set()` documentation

## 🚀 0.4.0 (2023-10-13)

### 🐛 Bug fixes

- **version**: update versionning to support `pdm` 2.8+
- support pre Python 3.9 importlib.resources.files

### 📖 Documentation

- **README**: improve typing and add some examples

### 📦 Build

- update CI/lint dependencies
- drop support for Python 3.7 and add Python 3.12
- update dependencies

## 🚀 0.2.0 (2023-06-22)

### 📖 Documentation

- **README**: add the initial documentation to the README

### 🧹 Chores

- **defaults**: use sane default values and expose them at package level
- **env**: test `GIT_` prefixed env vars cleaning
- **plugin**: remove the unused `run` helper
- **typing**: expose `GitConfig` type at package level

## 🚀 0.1.1 (2023-06-17)

### 📦 Build

- **metadata**: fix project PEP621 metadata and entrypoint plugin name

## 🚀 0.1.0 (2023-06-16)

### 💫 New features

- initial version with a single `gitconfig` session fixture