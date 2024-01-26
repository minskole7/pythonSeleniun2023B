import pytest
import math

def test_sqrt():
    num = 25
    assert 5 == math.sqrt(num)

def test_number():
    num = 25
    assert 5 == 3

def test_string():
    first_name = "aman"
    assert first_name.startswith("a")


# pip install pytest
# test_one.py
# two_test.py
# py.test
# py.test -v
# test method name should start with test_
# py.test -v .\test_demoOne.py running one particular file
# adding a marker to a testcase  "@pytest.mark.homePage"
# py.test -m homePage