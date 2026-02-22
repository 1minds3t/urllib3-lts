```markdown
# urllib3-lts-py37 🛡️

**Security Backport for Python 3.7**
Base: `urllib3 v2.0.7` | Patch Level: `2026.21441`

## 🚨 Security Fixes Included
This release backports fixes for **5 Critical/High/Moderate Vulnerabilities** found in the official `v2.0.7` release.

| CVE ID | Severity | Description | Status |
|:---|:---|:---|:---|
| **CVE-2026-21441** | 🔴 HIGH | **Decompression/Retry DoS:** Guarded redirect streaming & capped Retry-After. | 🛡️ **FIXED** |
| **CVE-2025-66471** | 🔴 HIGH | **Compression Bomb DoS:** Added `max_length` limits to decompression. | 🛡️ **FIXED** |
| **CVE-2025-66418** | 🔴 HIGH | **Unbounded Links:** Limited decompression chain depth. | 🛡️ **FIXED** |
| **CVE-2025-50181** | 🟡 MOD | **Redirect Bypass:** Fixed retry logic when redirects disabled. | 🛡️ **FIXED** |
| **CVE-2024-37891** | 🟡 MOD | **Header Leak:** Strips Proxy-Authorization on redirect. | 🛡️ **FIXED** |

## 📦 Installation
```bash
pip install urllib3-lts-py37==2026.21441
```

## 🌐 The OmniPKG Ecosystem
Maintained by **1minds3t**.

**Manage your environment:**
```bash
pip install omnipkg
omnipkg reset -y
```

## ⚠️ Installation Warning

**Uninstall urllib3 before installing this package:**

```bash
pip uninstall urllib3 -y
pip install urllib3-lts-py37
```

This ensures the security patches are applied and not overwritten.
```