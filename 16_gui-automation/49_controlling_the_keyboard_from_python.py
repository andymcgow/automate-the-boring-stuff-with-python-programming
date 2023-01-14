import pyautogui

# Send virtual keypresses: -
pyautogui.typewrite("Hello world!")

# NOTE you will need to have the window that you want to enter text into FOCUSED and ACTIVE.
# You can use mouse control to move to a new window, then by using the ; semi-colon symbol,
# you can have Python to run 2 bits of code from the same line (as once you've clicked away you can't run the rest of your code!)
pyautogui.click(100,100); pyautogui.typewrite("Hello world!")

# Like with mouse movement, you can delay the input of keypresses: -
pyautogui.typewrite("MESSAGE", interval=0.2)

# You can pass a list of strings as keypresses: -
# NOTE here how "left" is a string name that will acutally move the cursor to the left with the left arrow.
# By passing a list of strings to typewrite() you can perform hard-to-type keys like "shift".
pyautogui.typewrite(["a", "b", "left", "left", "X", "Y"])

# A single keypress can be done: -
pyautogui.press("f1")

# Hot keys can also be passed: -
pyautogui.hotkey("ctrl", "o")
