from recursion_package import __version__
from recursion_package.recursion_module import factorial, factorial_while


def test_version():
    assert __version__ == "0.1.0"


def test_factorial_one():
    actual = factorial(1)
    expected = 1
    assert actual == expected


def test_factorial_two():
    actual = factorial(2)
    expected = 2
    assert actual == expected


def test_factorial_3():
    actual = factorial(3)
    expected = 6
    assert actual == expected


def test_factorial_4():
    actual = factorial(4)
    expected = 24
    assert actual == expected


def test_factorial_5():
    actual = factorial(5)
    expected = 120
    assert actual == expected


def test_factorial_while_5():
    actual = factorial_while(5)
    expected = 120
    assert actual == expected
