# Security Analysis & Patch Tracking (urllib3-lts)

This directory tracks the security vulnerabilities (CVEs) affecting legacy versions of `urllib3` and documents the backported patches applied to maintain the `urllib3-lts` distributions for end-of-life Python versions (3.7, 3.8).

**Upstream Base Version:** `2.0.7` (Python 3.7 LTS) / `2.2.3` (Python 3.8 LTS)

---

## 🚨 CVE-2026-21441 (GHSA-38jv-5279-wg99)

* **Severity:** HIGH
* **Published:** 2026-01-07
* **Upstream Fix:** `2.6.3`
* **LTS Status:** Patched ✅

### Vulnerability Description
When following HTTP redirects using the streaming API, `urllib3` failed to properly maintain decoding state flags. This allowed malicious servers to bypass decompression-bomb (e.g., gzip, brotli, zstd) safeguards by chaining redirects, potentially leading to memory exhaustion and Denial of Service (DoS).

Additionally, the `Retry-After` header parsing lacked a strict upper bound, allowing malicious servers to dictate unreasonable backoff times.

### Impact on LTS Branches
The base versions used for Python 3.7 (`2.0.7`) and Python 3.8 (`2.2.3`) are both vulnerable as they predate the `2.6.3` upstream patch.

### Backport Strategy & Fix Details
The patch (`security/patches/cve-2026-21441.patch`) was manually backported from upstream `main` and applies two critical defenses:

1. **Decoding State Preservation (`response.py`):**
   During connection release (which happens implicitly during redirects when unread data is flushed), `self.read()` is now strictly instructed *not* to spend resources decoding content unless decoding had already been explicitly initiated (`decode_content=self._has_decoded_content`). This prevents the decompression bomb trigger.

2. **Retry-After Upper Bound (`util/retry.py`):**
   Introduced `DEFAULT_RETRY_AFTER_MAX` (21,600 seconds / 6 hours). Any `Retry-After` header exceeding this limit is now forcibly clamped to 6 hours, preventing integer overflows or indefinite hangs in worker threads processing redirects.

---

*Note: All patches in the `security/patches/` directory are generated via `diff -u` and applied automatically via the CI/CD pipeline or `omnipatcher` during build time.*
