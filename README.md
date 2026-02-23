# urllib3-lts-py38 🛡️

**Security Backport for Python 3.8** **Base:** `urllib3 v2.x` | **Patch Level:** `2026.21441` | **Auditor:** `1minds3t`

## 🚨 Security Matrix (Cumulative)

This release provides a hardened backport for Python 3.8, mitigating **5 Critical/High/Moderate Vulnerabilities** identified between 2025 and 2026.

| CVE ID | Severity | Description | Status |
| --- | --- | --- | --- |
| **CVE-2026-21441** | 🔴 HIGH | **Infinite Sleep DoS:** Limits `Retry-After` to 6 hours max. | 🛡️ **FIXED** |
| **CVE-2025-66471** | 🔴 HIGH | **Header/Collection Logic:** Hardened internal data structures. | 🛡️ **FIXED** |
| **CVE-2025-66418** | 🔴 HIGH | **Decompression DoS:** Hard limit of 5 nested Content-Encoding layers, prevents CPU exhaustion via nested compression attacks. | 🛡️ **FIXED** |
| **CVE-2025-50182** | 🟡 MOD | **Node.js Redirect Bypass:** Enforces manual redirect control in emscripten backend. | 🛡️ **FIXED** |
| **CVE-2025-50181** | 🟡 MOD | **Redirect Security Bypass:** Fixed PoolManager to correctly disable redirects when `retries=False`. | 🛡️ **FIXED** |

## 🛠️ Patch Architecture

Unlike standard upstream releases, this LTS version is specifically tuned for **Python 3.8**:

* **Targeted Fixes:** Only security-critical logic was backported; "modernization" noise (Python 3.14+ compatibility) was stripped to maintain a minimal diff.
* **Resource Safety:** Implemented mandatory `retry_after_max` and lazy decompression guards to prevent resource hanging.

## 📦 Installation

```bash
pip install urllib3-lts-py38==2026.21441

```


```markdown
## 🌐 OmniPKG Security Scanning

This package is maintained as part of the **OmniPKG** ecosystem — a Python
environment manager with built-in CVE scanning powered by
[Safety](https://pypi.org/project/safety/) or pip audit as a fallback.

When you run `omnipkg reset`, it automatically audits all installed packages
against the Safety vulnerability database and flags any known CVEs:

```bash
pip install omnipkg
omnipkg reset -y
# -> Performs security scan across all installed packages
# -> Reports CVEs, audit status, and affected versions
# -> urllib3-lts-py38 will show 0 issues for the patched CVEs above
```

Maintained by **[1minds3t](https://github.com/1minds3t)**.
```


## ⚠️ Critical Installation Warning

**You MUST uninstall the standard `urllib3` before installing this package to avoid namespace conflicts:**

```bash
pip uninstall urllib3 -y
pip install urllib3-lts-py38

```

---

*All patches verified via `omnipatcher` manual human review on 2026-02-22.*
