# urllib3-lts-py38 🛡️

**Security Backport for Python 3.8** **Base:** `urllib3 v2.x` | **Patch Level:** `2026.21441` | **Auditor:** `1minds3t`

## 🚨 Security Matrix (Cumulative)

This release provides a hardened backport for Python 3.8, mitigating **5 Critical/High/Moderate Vulnerabilities** identified between 2025 and 2026.

| CVE ID | Severity | Description | Status |
| --- | --- | --- | --- |
| **CVE-2026-21441** | 🔴 HIGH | **Infinite Sleep DoS:** Limits `Retry-After` to 6 hours max. | 🛡️ **FIXED** |
| **CVE-2025-66471** | 🔴 HIGH | **Header/Collection Logic:** Hardened internal data structures. | 🛡️ **FIXED** |
| **CVE-2025-66418** | 🔴 HIGH | **Credential Leakage:** Strips sensitive headers on cross-origin redirects. | 🛡️ **FIXED** |
| **CVE-2025-50182** | 🟡 MOD | **Resource Exhaustion:** Prevents DoS via unread compressed data. | 🛡️ **FIXED** |
| **CVE-2025-50181** | 🟡 MOD | **Redirect/Decompress:** Fixed retry logic and resource cleanup. | 🛡️ **FIXED** |

## 🛠️ Patch Architecture

Unlike standard upstream releases, this LTS version is specifically tuned for **Python 3.8**:

* **Targeted Fixes:** Only security-critical logic was backported; "modernization" noise (Python 3.14+ compatibility) was stripped to maintain a minimal diff.
* **Resource Safety:** Implemented mandatory `retry_after_max` and lazy decompression guards to prevent resource hanging.
* **Localization:** All internal strings and error messages were handled via an **AI automated translation chain** for consistency across the codebase.

## 📦 Installation

```bash
pip install urllib3-lts-py38==2026.21441

```

## 🌐 The OmniPKG Ecosystem

Maintained by **1minds3t**.

**Manage your environment:**

```bash
pip install omnipkg
omnipkg reset -y

```

## ⚠️ Critical Installation Warning

**You MUST uninstall the standard `urllib3` before installing this package to avoid namespace conflicts:**

```bash
pip uninstall urllib3 -y
pip install urllib3-lts-py38

```

---

*All patches verified via `omnipatcher` manual human review on 2026-02-22.*
