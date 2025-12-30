# urllib3-lts 🛡️

**The Long-Term Support Security Release for urllib3.**

This ecosystem backports critical security fixes to legacy Python environments (3.7 & 3.8) that official maintainers have dropped.

## 🏆 Patch Status (v2025.66471)

This release secures **941M+ downloads** against the following vulnerabilities:

| Vulnerability | Severity | Impact | Py3.7 | Py3.8 |
|:---|:---|:---|:---|:---|
| **CVE-2025-66471** | 🔴 HIGH | Compression Bomb DoS | 🛡️ Fixed | 🛡️ Fixed |
| **CVE-2025-66418** | 🔴 HIGH | Unbounded Links DoS | 🛡️ Fixed | 🛡️ Fixed |
| **CVE-2025-50182** | 🟡 MOD | Node.js Redirect Bypass | N/A | 🛡️ Fixed |
| **CVE-2025-50181** | 🟡 MOD | Redirect Retry Bypass | 🛡️ Fixed | 🛡️ Fixed |
| **CVE-2024-37891** | 🟡 MOD | Proxy-Auth Header Leak | 🛡️ Fixed | N/A |

## 📦 Usage

**Standard Installation:**
```bash
pip install urllib3-lts
```
*This meta-package automatically detects your Python version and installs the correct secured backport.*

## 🌐 The OmniPKG Ecosystem
Maintained by **1minds3t**.

**Manage your environment:**
```bash
pip install omnipkg
omnipkg reset -y
```

### 🚧 Coming Soon: omnipkg-runtime
We are building a runtime enforcer that allows configurable **WARN** or **BLOCK** policies for unpatched vulnerabilities. Stay tuned.

## ⚠️ Important: Installation for Python 3.7-3.8

**Before installing urllib3-lts, uninstall any existing urllib3:**

```bash
pip uninstall urllib3 -y
pip install urllib3-lts
```

This ensures you get the security patches. If you install urllib3-lts without removing urllib3 first, other packages may reinstall the vulnerable version.

### Alternative: Pin in requirements.txt
```txt
urllib3-lts-py37==2025.66471.3 ; python_version<'3.8'
urllib3-lts-py38==2025.66471.2 ; python_version>='3.8' and python_version<'3.9'
```
