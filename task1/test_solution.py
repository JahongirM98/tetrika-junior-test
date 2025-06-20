import pytest
from solution import strict

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

@strict
def concat(a: str, b: str) -> str:
    return a + b

def test_sum_two_valid():
    assert sum_two(1, 2) == 3

def test_sum_two_invalid_type():
    with pytest.raises(TypeError):
        sum_two(1, 2.4)

def test_concat_valid():
    assert concat("hello", "world") == "helloworld"

def test_concat_type_error():
    with pytest.raises(TypeError):
        concat("hello", 123)
