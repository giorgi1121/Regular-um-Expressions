import pytest
from working import convert

def main():
    test_correct_time()
    test_format()
    test_hours()

def test_correct_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
        convert("09:00 AM - 17:00 PM")

def test_hours():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
        convert("9 AM to 15 PM")
        convert("14 AM to 17 PM")

def test_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
        convert("9:00 AM to 5:70 PM")

if __name__ == "__main__":
    main()