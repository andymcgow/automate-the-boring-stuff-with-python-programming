# Example of a function that WILL error out due to a ZeroDivisionError (no try/except).

# def div42by(divide_by):
#     return 42 / divide_by

# print(div42by(2))
# print(div42by(12))
# print(div42by(0))
# print(div42by(1))


# Example of the above function, fixed with a try/except statement.
# (Program continues when it gets to the ZeroDivisionError.)

def div42by(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print("Error: You tried to divide by zero.")

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))


# Another try/except example.

print("How many cats do you have?")
num_cats = input()
try:
    if int(num_cats) >= 4:
        print("That is a lot of cats.")
    else:
        print("That is not that many cats.")
except ValueError:
    print("You did not enter a number.")