def fizzify(num):
    """
    For number divisible by 3 return Fizz
    For number divisible by 5 return Buzz
    For number divisible by 5 and 3 return FizzBuzz
    All other numbers return the given number as string
    """
    word = ""

    if num % 3 == 0:
        word = "Fizz"

    if num % 5 == 0:
        word += "Buzz"

    # return the "word" if there is one otherwise return string of number
    return word or str(num)



def fizzify_another_way(num):
    if num % 5 == 0 and num % 3 == 0:
        return "FizzBuzz"

    if num % 3 == 0:
        return "Fizz"

    if num % 5 == 0:
        return "Buzz"


    return str(num)
