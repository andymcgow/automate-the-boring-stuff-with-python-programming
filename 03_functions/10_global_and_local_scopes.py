spam = 42 # Global Variable

def eggs():
    spam = 42 # Local Variable


# Example of local variable being unreachable in a global scope.

# def spam():
#     eggs = 99

# spam()
# print(eggs)


# Example of 2 different local variables using the same name, but independently of each other.

# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)

# def bacon():
#     ham = 101
#     eggs = 0

# spam()
# print(eggs)


# Example of a global varaible being accessed in a local scope.

# def spam():
#     print(eggs)

# eggs = 42
# spam()


# Example of a locally defined variable overriding a globally defined variable inside of a function.

# def spam():
#     eggs = "Hello"
#     print(eggs)

# eggs = 42
# spam()
# print(eggs)


# Example of changing a global variable inside of a function. (Using the 'global' keyword)
# !!! THIS IS CONSIDERED BAD PRACTICE !!!
# Use a parameter for passing a value onto a function or return a value to obtain it instead.

def spam():
    global eggs
    eggs = "Hello"
    print(eggs)

eggs = 42
spam()
print(eggs)
