# You can raise your own exceptions to handle errors and print your own message: -
# raise Exception("This is the error message.")

# In this 'box printing' program below, there is a raise Exception to handle if a symbol is passed over with a len() greater than 1: -
# (A symbol with a len() greater than 1 will break the below code so the ASCII art that is printed won't look like a box.)  
def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("Symbol needs to be a string of length 1.")
    if (width < 2) or (height < 2):
        raise Exception("'Width' and 'Height' must be greater or equal to 2.")
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (" " * (width - 2)) + symbol)
    print(symbol * width)

box_print("*", 15, 5)
box_print("o", 5, 15)

# box_print("**", 15, 5)
# box_print("*", 1, 1)

# The traceback.format_exc() function allows you to write error messages and tracebacks to a file.
# NOTE you will need to import traceback to use traceback.format_exc() : -
import traceback

try:
    raise Exception("This is the error message.")
except:
    error_file = open("error_log.txt", "a")
    error_file.write(traceback.format_exc())
    error_file.close()
    print("The traceback info was written error_log.txt")


# Assertions and the assert statement is a santiy check to make sure your code isn't doing something obviosuly wrong: -
# assert False, "This is the error message."

# In the below example, a simple traffic light switching program,
# there is an assert statement to make sure at least one of the lights is red: -
market_2nd = {"ns": "green", "ew": "red"}

def switch_lights(intersection):
    for key in intersection.keys():
        if intersection[key] == "green":
            intersection[key] = "yellow"
        elif intersection[key] == "yellow":
            intersection[key] = "red"
        elif intersection[key] == "red":
            intersection[key] = "green"
    assert "red" in intersection.values(), "Neither light is red!" + str(intersection)

switch_lights(market_2nd)

# NOTE Assertions are from programmer errors, (to help fix bugs and code), not user errors.
# User errors should raise exceptions.
