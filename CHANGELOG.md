# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2026.21441.1] — 2026-02-22

Metadata and Packaging Cleanup

**Maintenance Release**
**Base:** `urllib3 v2.2.3` | **Patch Level:** `2026.21441.1`

This release addresses packaging metadata issues and documentation inaccuracies found immediately after the v2026.21441 security release. No functional code changes were made to the library logic.

*   **Added `MANIFEST.in`:** Ensures `CHANGES.rst` and other critical project files are correctly included in the source distribution (sdist).
*   **Cleaned Repo Metadata:** Removed stale `PKG-INFO` files that contained outdated upstream metadata.
*   **Updated `.gitignore`:** Added rules for build artifacts, coverage files, and test reports.

*   **README Corrections:** Fixed descriptions for CVE-2025-66418, CVE-2025-50182, and CVE-2025-50181 in the security matrix to accurately reflect the backported mitigations.
*   **Clarification:** Removed inaccurate references to "AI translation chains" in the patch architecture description.
*   **OmniPKG:** Updated security scanning details to mention `pip-audit` fallback.

```bash
pip install urllib3-lts-py38==2026.21441.1
```

---

**📚 Documentation:**
- README.md (24 lines)

**⚙️ Configuration:**
- pyproject.toml (2 lines)

_5 files changed, 86 insertions(+), 163 deletions(-)_

## [2026.21441] — 2026-02-22

Finalize 5-CVE Security Backport Chain for Python 3.8

Completes the security backport chain for the Python 3.8 LTS stream of
urllib3 v2.2.3. All 5 target CVEs are now patched and verified against a
dedicated security test suite (105 passed, 3 skipped).

Security fixes included:
- CVE-2026-21441: Retry-After DoS cap (DEFAULT_RETRY_AFTER_MAX=21600s) and
  decompression bomb guard in drain_conn()
- CVE-2025-66471: HTTPHeaderDict bytes key handling (__getitem__, __delitem__,
  __contains__, getlist) and streaming decompression limits
- CVE-2025-66418: Hard limit of 5 nested Content-Encoding layers
- CVE-2025-50181: Redirect disabled correctly when retries=False
- CVE-2025-50182: Manual redirect enforcement in emscripten/Node.js backend

Backport integrity: 209 lines changed vs vanilla urllib3 v2.2.3 baseline.
No modern Python (3.14+) stdlib imports. No typing incompatibilities.
Verified clean via upstream tarball diff.

---

**📝 Code Changes:**
- NEW: setup.py (3 lines changed)
- UPDATE: src/urllib3/_collections.py (20 lines changed)
- NEW: src/urllib3/_version.py (5 lines changed)
- UPDATE: src/urllib3/contrib/emscripten/__init__.py (17 lines changed)
- UPDATE: src/urllib3/contrib/emscripten/connection.py (255 lines changed)
- UPDATE: src/urllib3/response.py (225 lines changed)
- UPDATE: src/urllib3/util/retry.py (22 lines changed)

**🧪 Tests:**
- NEW: test/security/

**📚 Documentation:**
- README.md (50 lines)

**⚙️ Configuration:**
- .github/workflows/publish.yml (86 lines)
- pyproject.toml (19 lines)

_114 files changed, 21869 insertions(+), 3608 deletions(-)_
