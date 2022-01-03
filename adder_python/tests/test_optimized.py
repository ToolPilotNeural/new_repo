import pytest
import adder

add_test_oracle = [
    (1, 1, 2),
    (-1, -1, -2),
    (-1, 1, 0),
    (1, 0, 1),
    (-1, 0, -1)
]

subtract_test_oracle = [
    (1, 1, 0),
    (-1, -1, 0),
    (-1, 1, -2),
    (1, 0, 1),
    (-1, 0, -1)
]

multiply_test_oracle = [
    (2, 2, 4),
    (-2, -2, 4),
    (-2, 2, -4),
    (2, 0, 0),
    (-2, 0, 0),
    (-2, 1, -2),
    (2, 1, 2)
]

divide_test_oracle = [
    (2, 1, 2),
    (-2, -1, 2),
    (-2, 1, -2),
    (2, -1, -2),
    (-2, 2, -1),
    (2, 2, 1),
    (2, -2, -1),
    (-2, 2, -1),
    (-2, -2, 1)
]


# Testing sum function
@pytest.mark.parametrize('num1, num2, result', add_test_oracle)
def test_add_two_numbers(num1, num2,result):
    assert adder.add_two_numbers(num1, num2) == result


# Testing subtraction function
@pytest.mark.parametrize('num1, num2, result', subtract_test_oracle)
def test_subtract_two_numbers(num1, num2,result):
    assert adder.subtract_two_numbers(num1, num2) == result


# Testing multiplication function
@pytest.mark.parametrize('num1, num2, result', multiply_test_oracle)
def test_multiply_two_numbers(num1, num2,result):
    assert adder.multiply_two_numbers(num1, num2) == result


# Testing division function
@pytest.mark.parametrize('num1, num2, result', divide_test_oracle)
def test_divide_two_numbers(num1, num2,result):
    assert adder.divide_two_numbers(num1, num2) == result

def test_divide_two_numbers_positive_and_zero():
    with pytest.raises(Exception):
        assert adder.divide_two_numbers(2, 0)

def test_divide_two_numbers_negative_and_zero():
    with pytest.raises(Exception):
        assert adder.divide_two_numbers(-2, 0)