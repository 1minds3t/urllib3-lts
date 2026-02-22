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

### Backport Strategy & Fix Details
1. **Decoding State Preservation (`response.py`):** `self.read()` is now strictly instructed *not* to spend resources decoding content unless decoding had already been explicitly initiated (`decode_content=self._has_decoded_content`).
2. **Retry-After Upper Bound (`util/retry.py`):** Introduced `DEFAULT_RETRY_AFTER_MAX` (21,600 seconds / 6 hours). Any `Retry-After` header exceeding this limit is forcibly clamped.

---

## 🚨 CVE-2025-66471 (GHSA-h2h8-8vqw-qf8j)

* **Severity:** HIGH
* **Upstream Fix:** `2.6.0`
* **LTS Status:** Patched ✅

### Vulnerability Description
Unbounded memory consumption when reading highly compressed responses via the streaming API (`read(amt=N)`). The socket read was throttled, but the decompressor was not, turning small compressed reads into gigabytes of memory allocation.

### Backport Strategy & Fix Details
* Added `max_length` parameter to all internal decoders (zlib, brotli) and enforced it via `HTTPResponse._decode()`.
* **Py3.7 Regression Fix:** Manually added `latin-1` decode guards in `src/urllib3/_collections.py` to `HTTPHeaderDict` methods to handle `bytes` keys passed internally by Python 3.7's legacy `http.client`.

---

## 🚨 CVE-2025-66418 (GHSA-7xwx-4586-3mhc)

* **Severity:** HIGH
* **Upstream Fix:** `2.6.0`
* **LTS Status:** Patched ✅

### Vulnerability Description
Infinite recursion and resource exhaustion via malicious `Content-Encoding` headers. A server could send thousands of comma-separated encodings, forcing `urllib3` to allocate thousands of chained decompressor objects.

### Backport Strategy & Fix Details
* Hardcoded a strict maximum of 5 decode links inside `MultiDecoder.max_decode_links`.

---

## 🟡 CVE-2025-50181 (GHSA-pq67-xjf6-5j8g)

* **Severity:** MODERATE
* **Upstream Fix:** `2.5.0`
* **LTS Status:** Patched ✅

### Vulnerability Description
When instantiating `PoolManager(retries=False)`, HTTP redirects were not properly disabled, leaving applications vulnerable to Server-Side Request Forgery (SSRF) bypasses.

### Backport Strategy & Fix Details
* Fixed `PoolManager` initialization to properly convert boolean flags to a `Retry` instance with a `redirect=0` budget.

---

## 🟡 CVE-2024-37891 (GHSA-34jh-p97f-mpxf)

* **Severity:** MODERATE
* **Upstream Fix:** `2.2.2`
* **LTS Status:** Patched ✅

### Vulnerability Description
Cross-origin credential leak. The `Proxy-Authorization` header was not automatically stripped when following redirects to a different origin.

### Backport Strategy & Fix Details
* Added `"Proxy-Authorization"` to `Retry.DEFAULT_REMOVE_HEADERS_ON_REDIRECT`.

---

*Note: All patches in the `security/patches/` directory are generated via `diff -u` and applied automatically via the CI/CD pipeline or `omnipatcher` during build time.*