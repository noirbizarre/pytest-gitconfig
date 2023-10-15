# Changelog

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
