# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2026.21441] — 2026-02-22

Finalize 5-CVE Backport Chain for Python 3.7 and 3.8

Completes the CVE-2026-21441 backport cycle for Python 3.7 and 3.8 LTS
streams. Meta-package updated to pull verified patched sub-packages.

Sub-package coverage (cumulative):
- urllib3-lts-py37 v2026.21441.1 — Python 3.7 (502M monthly downloads)
- urllib3-lts-py38 v2026.21441   — Python 3.8 (426M monthly downloads)

Security fixes included in this release chain:
- CVE-2026-21441: Retry-After DoS cap + decompression bomb in drain_conn()
- CVE-2025-66471: HTTPHeaderDict bytes key hardening + streaming limits
- CVE-2025-66418: Hard limit of 5 nested Content-Encoding layers
- CVE-2025-50182: Manual redirect enforcement in emscripten/Node.js
- CVE-2025-50181: Redirect correctly disabled when retries=False
- CVE-2024-37891: Proxy-Auth header leak (py37 only)

Note: Python 3.9 coverage (CVE-2026-21441, 751M downloads) is pending
urllib3-lts-py39 — dispatcher will be updated with a .1 suffix release
once that backport is complete.

Dispatcher branch cleaned: removed all leaked working files, stale
upstream src/urllib3/ tree, test/, and dummyserver/.

---

**📝 Code Changes:**
- NEW: src/urllib3_lts/setup.py (2 lines changed)

**📚 Documentation:**
- LICENSE.txt
- README.md (38 lines)

**⚙️ Configuration:**
- .github/workflows/publish.yml (37 lines)
- pyproject.toml (20 lines)

**Additional Changes:**
- ci(workflow): add py39 support and robust OIDC/token publish fallback
- chore: bump toml
- chore: strip dispatcher to meta-package only

**Bug Fixes:**
- fix: add __init__.py to make meta-package importable
- fix: remove fake metadata build step that caused PyPI auth failure

**Updates:**
- Update pyproject.toml
- Update publish.yml

_267 files changed, 227 insertions(+), 80293 deletions(-)_
