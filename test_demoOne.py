import pytest
import math

def test_sqrt():
    num = 25
    assert 5 == math.sqrt(num)

def test_number():
    num = 25
    assert 5 == 5

def test_string():
    first_name = "aman"
    assert first_name.startswith("a")
