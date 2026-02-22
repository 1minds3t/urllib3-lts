"""
Shared fixtures for urllib3-lts security tests.
Run all security tests: pytest tests/security/ -v
"""
import sys
from pathlib import Path

# Always test OUR src/, not any installed version
_SRC = Path(__file__).parent.parent.parent / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))
