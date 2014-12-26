import pytest

from evaluate_reverse_polish_notation import Solution


@pytest.fixture
def solve():
    return Solution().evalRPN


@pytest.mark.parametrize(['input', 'expected'], [
    (["10","6","9","3","+","-11","*","/","*","17","+","5","+"],
        22),
    (["2", "1", "+", "3", "*"],
        9),
    (["4", "13", "5", "/", "+"],
        6),
])
def test(input, expected, solve):
    assert solve(input) == expected
