# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2026.21441] — 2026-02-22

Comprehensive Security Backports (CVE-2024-37891 to CVE-2026-21441)

This critical release delivers cumulative security backports for the Python 3.7 LTS branch of `urllib3`, addressing five distinct vulnerabilities spanning from mid-2024 to early 2026.

All patches have been meticulously adapted to maintain runtime compatibility with Python 3.7, stripping out structural refactors (like Python 3.14 imports or walrus operators) while preserving the core security logic.


* **[CVE-2026-21441] Decompression-Bomb Bypass & Retry-After DoS**
  * Patched `drain_conn()` to respect the caller's decoding state, preventing decompression bombs from exhausting resources when following HTTP redirects via the streaming API.
  * Implemented a strict 6-hour (`21600` second) maximum cap on `Retry-After` headers to prevent malicious servers from causing indefinite sleep DoS attacks.
* **[CVE-2025-66471] Streaming API Unbounded Decompression**
  * Bounded zlib and brotli decoders via the `max_length` parameter to safely throttle memory usage when processing highly compressed payloads chunk-by-chunk.
  * **Core Regression Fixed:** Manually applied `latin-1` decoding guards to `__getitem__`, `__delitem__`, `__contains__`, and `getlist` inside `_collections.py`. This ensures `HTTPHeaderDict` safely handles `bytes` keys passed internally by Python 3.7's `http.client`.
* **[CVE-2025-66418] MultiDecoder Infinite Chain Resource Exhaustion**
  * Hardcoded a strict maximum of 5 decode links inside `MultiDecoder` to prevent a malicious server from triggering massive memory allocation via infinitely chained `Content-Encoding` headers.
* **[CVE-2025-50181] Open Redirect via PoolManager**
  * Fixed an issue where instantiating a `PoolManager` with `retries=False` or `retries=0` failed to properly disable redirects, leaving applications vulnerable to SSRF.
* **[CVE-2024-37891] Proxy-Authorization Header Leak**
  * Added `Proxy-Authorization` to the default list of headers that are automatically stripped during cross-origin redirects.


* **Build Support:** Added a minimal `setup.py` shim to fully support `pip install -e .` on legacy `pip` and `setuptools` versions prevalent in Python 3.7 environments that lack complete PEP 660 (`pyproject.toml`) support.
* **Security Test Suite:** Backported and stabilized 110 dedicated security tests specifically targeted at verifying these CVEs. All tests now pass cleanly under CPython 3.7.9.
* **Documentation:** Introduced a dedicated `security/ANALYSIS.md` to track vulnerability patch diffs and justify LTS backport divergence (e.g., omitted typing modernizations).

---

**📝 Code Changes:**
- NEW: setup.py (5 lines changed)
- UPDATE: src/urllib3/_collections.py (10 lines changed)
- UPDATE: src/urllib3/response.py (6 lines changed)
- UPDATE: src/urllib3/util/retry.py (20 lines changed)

**🧪 Tests:**
- NEW: test/security/

**📚 Documentation:**
- security/ANALYSIS.md (35 lines)

**⚙️ Configuration:**
- pyproject.toml (7 lines)

**Additional Changes:**
- security: finalize backports for CVE-2024-37891 through CVE-2026-21441 (Py3.7 LTS)
- fix: Bump version/prepare for next CVE patch.
- docs: add vulnerability analysis and patch documentation for CVE-2026-21441
- fix: patch CVE-2026-21441 decompression-bomb bypass

_40 files changed, 14564 insertions(+), 5 deletions(-)_

