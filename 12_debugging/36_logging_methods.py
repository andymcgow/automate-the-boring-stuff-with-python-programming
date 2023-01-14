# Logging is a great way to understand what's happening in your program and when.
# NOTE you will need to import logging: -
import logging

# Setup code for a basic logging string in Python: -
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

# If you want to save log messages to a file, modify the above code to include a pathname, like below: -
# NOTE with this option enable, none of the messages will be displayed on the screen and ONLY saved in the file.
# logging.basicConfig(filename="program_log.txt", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


# There are 5 log levels: -
# DEBUG     (Lowest)
# INFO
# WARNING
# ERROR
# CRITICAL  (Highest)


# If you want to turn off logging, rather than commenting out logging.debug() code you can instead at the top of your file call: -
# logging.disable(logging.CRITICAL)
# NOTE the log level passed through in the argument will disable that AND ALL other levels below, so CRITICAL turns off all logging.


logging.debug("Start of program")

def factorial(n):
    logging.debug("Start of factorial(%s)" % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug("i is %s, total is %s" % (i, total))
    logging.debug("Return value is %s" % (total))
    return total

print(factorial(5))

logging.debug("End of program")
