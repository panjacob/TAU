import pytest

from fibonacci import fib

test_data = [(-500, None), (0.5, None), (-22.123, None), (fib, None), ([1, 2, 3], None), (0, 0), (1, 1),
             (2, 1), (3, 2), (19, 4181), (31, 1346269), ("5", None), (float('inf'), None), (float('-inf'), None)]


@pytest.mark.parametrize("number,expected", test_data)
def test_fibonacci(number, expected):
    assert fib(number) == expected
