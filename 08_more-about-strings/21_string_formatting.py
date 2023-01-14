# Simple string concatonation can be done with +
print("hello " + "world")

name = "Alice"
place = "Main Street"
time = "6 pm"
food = "turnips"

# This gets complicated if you are using a lot of strings: -
print("Hello " + name + ", you are invited to a party at " + place + " at " + time + ". Please bring " + food + ".")

# Python has String Formatting, also called String Interpolation to allow us to use the %s Conversion Specifier to simpify our code: -
print("Hello %s, you are invited to a party at %s at %s. Please bring %s." % (name, place, time, food))