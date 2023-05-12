import pytest
from um import count

def main():
    test_separate_um()
    test_substring_um()
    test_white_space()
    test_case_insensitive()

def test_separate_um():
    assert count("um, thanks, um...") == 2

def test_substring_um():
    assert count("yummy") == 0

def test_white_space():
    assert count("   um   ") == 1

def test_case_insensitive():
    assert count("Hello, UM, it is very YUAMY") == 1

if __name__ == "__main__":
    main()