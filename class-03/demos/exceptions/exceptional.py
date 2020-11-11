
# print("let's do something totally wrong. See if you can spot me in the output!")
# print("Too many parentheses")


# print("More wrongness. Do I get printed?")
# print('Who has ever "messed up" quotations marks?')


# print("What happens now? Do you see me printed?")

# denomimator = 1
# value = 1/denomimator

# try:
#     print("Divide by zero again", 1 / 0)
# except ZeroDivisionError:
#     print("Don't divide by zero silly.")

# print("handled the exception above, carrying on")



# denominator = "spam"

# try:
#     print("Divide by zero again", 1 / denominator)
# except:
#     print("Don't divide by zero silly.")

# print("Total lie!. The problem was not dividing by zero. It was a type error")


try:
    spam = "nonsense" / 42
except ZeroDivisionError:
    print("Don't divide by zero silly.")
except TypeError:
    print("Wrong type silly")
except Exception as e:  # notice we can refer to the exception using 'as'
    # log the exception somewhere, probably including the stack trace
    print("So sorry end user. Something broke!")
finally:
    print(" I ALWAYS run")



age = -10

if age < 0:
    raise ValueError("Invalid age - must be greater than or equal to zero")




class SocialDistanceError(Exception):
    def __init__(self, distance):
        super().__init__(f"Stay 6 feet away, not {distance}")


distance_feet = 4

if distance_feet < 6:
    raise SocialDistanceError(distance_feet)
