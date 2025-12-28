# urllib3-lts 🛡️
**Security Backports for Legacy Python.**

## Latest Release: CVE-2025-66471 & CVE-2025-66418
**Critical Decompression DoS Protection**

| Vulnerability | Severity | Py3.7 | Py3.8 | Py3.9+ |
|:---|:---|:---|:---|:---|
| **CVE-2025-66471** (Compression Bomb) | 🔴 HIGH | 🛡️ Fixed | 🛡️ Fixed | ✅ Native |
| **CVE-2025-66418** (Chain Limit) | 🔴 HIGH | 🛡️ Fixed | 🛡️ Fixed | ✅ Native |
| **CVE-2025-50182** (Node.js Redirects) | 🟡 MOD | N/A | 🛡️ Fixed | ✅ Native |
| **CVE-2025-50181** (Redirect Disable) | 🟡 MOD | 🛡️ Fixed | 🛡️ Fixed | ✅ Native |
| **CVE-2024-37891** (Proxy-Auth Leak) | 🟡 MOD | 🛡️ Fixed | ✅ Native | ✅ Native |

## Installation
```bash
pip install urllib3-lts
```

Automatically installs the correct secured version for your Python runtime.

## What's Fixed

### CVE-2025-66471 (HIGH) - Compression Bomb DoS
Attackers could send highly compressed data (1KB → 1GB) to exhaust memory. Fixed by:
- Adding bounded decompression with `max_length` parameter
- Limiting decompression per chunk to prevent memory exhaustion
- Tracking unconsumed data properly

### CVE-2025-66418 (HIGH) - Unbounded Decompression Chain
Attackers could chain unlimited encodings (`gzip,gzip,gzip,...`). Fixed by:
- Limiting decompression chain to maximum 5 links
- Raising `DecodeError` for excessive chaining

### Market Impact
- **Python 3.7**: 532M monthly downloads (9.23%)
- **Python 3.8**: 409M monthly downloads (7.09%)
- **Total**: 941M affected downloads secured

## License
MIT
