from fizz_buzz.fizz_buzz_module import fizzify

#    """
#     For number divisible by 3 return Fizz
#     For number divisible by 5 return Buzz
#     For number divisible by 5 and 3 return FizzBuzz
#     All other numbers return the given number as string
#     """

def test_import():
    assert fizzify


def test_fizzify_1():
    actual = fizzify(1)
    expected = "1"
    assert actual == expected

def test_fizzify_2():
    actual = fizzify(2)
    expected = "2"
    assert actual == expected


def test_fizzify_3():
    actual = fizzify(3)
    expected = "Fizz"
    assert actual == expected

def test_fizzify_4():
    actual = fizzify(4)
    expected = "4"
    assert actual == expected

def test_fizzify_5():
    actual = fizzify(5)
    expected = "Buzz"
    assert actual == expected

def test_fizzify_6():
    actual = fizzify(6)
    expected = "Fizz"
    assert actual == expected

def test_fizzify_10():
    actual = fizzify(10)
    expected = "Buzz"
    assert actual == expected

def test_fizzify_15():
    actual = fizzify(15)
    expected = "FizzBuzz"
    assert actual == expected


def test_fizzify_30():
    actual = fizzify(30)
    expected = "FizzBuzz"
    assert actual == expected
