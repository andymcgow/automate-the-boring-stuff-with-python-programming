# The webbrowser module only has one function, which opens web pages in your system's default browser: -
import webbrowser
webbrowser.open("https://automatetheboringstuff.com")


# The below program reads an address from the clipboard (or one passed through as an argument),
# then opens a web browser to a Google Maps page for that address.

import sys, pyperclip

sys.argv # ["mapit.py", "870", "Valencia", "St."]

# Check if command line arguments were passed
if len(sys.argv) > 1:
    # ["mapit.py", "870", "Valencia", "St."] -> "870 Valencia St."
    address = " ".join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.com/maps/place/<ADDRESS>
webbrowser.open("https://www.google.com/maps/place/" + address)
