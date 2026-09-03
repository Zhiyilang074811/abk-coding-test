import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from string_utils import reverse_string, to_uppercase

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"

def test_to_uppercase():
    assert to_uppercase("hello") == "HELLO"
    assert to_uppercase("") == ""
    assert to_uppercase("ABC") == "ABC"
