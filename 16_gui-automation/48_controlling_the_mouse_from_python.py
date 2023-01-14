import pyautogui

# Get screen resolution: -
print(pyautogui.size())
# NOTE even though screen resolution will be displayed accuately, I.E. 1280x720 or 1440x900, the screen coordinates start a 0,0.
# So the maximum range when inputting code for screen/cursor position, will always be 1 less than the maximum. (1279x719, etc)

# Setting width & height to variables: -
width, height = pyautogui.size()

# Fetching current position of the mouse cursor: -
print(pyautogui.position())

# Move the cursor: -
# (NOTE the cursor will instantly jump to this location!)
pyautogui.moveTo(10,10)
# To move a regular speed with some delay, as if a human was controlling the mouse, a time argument can be specified: -
pyautogui.moveTo(1429,889, duration=1.5)

# You can also move the mouse RELATIVE to where it currently is: -
pyautogui.moveRel(-200, 0)
# .moveRel() can also be passed a time arugment: -
pyautogui.moveRel(0, -100, duration=1)

# To make the mouse click: -
pyautogui.click(555, 10)

# Double click: -
pyautogui.doubleClick(555, 10)

# Right click: -
pyautogui.rightClick(555, 10)

# Middle click: -
pyautogui.middleClick(555, 10)

# If you don't pass coordinates, the mouse will click where it currently is: -
pyautogui.click()

# You can drag with left click by using: -
pyautogui.dragTo()
pyautogui.dragRel()

# You can loose control of your mouse using pyautogui, so as a fail safe it is programmed to raise an exception if the mouse goes to 0,0.
# If you need to exit/quit a pyautogui program, try slamming your mouse up and left.

# This can be run to get real-time feedback on mouse position, as well as RGB values from the pixels underneath the cursor.
# NOTE this must be run in the Terminal.
pyautogui.displayMousePosition()
