import pyautogui

# Take screenshots: -
pyautogui.screenshot()

# Save screenshots to disk: -
pyautogui.screenshot("screnshot_example.png")

# Pass through a cropped screenshot of an area of screen you want to find and coordinates and a region will be Returned: -
# NOTE screenshot's have to be a pixel perfect match to screen for area to be found!
pyautogui.locateOnScreen("CROPPED_SCREENSHOT.png")

# Find center of the region: -
pyautogui.locateCenterOnScreen("CROPPED_SCREENSHOT.png")

# Using image recognition you can write bots to play simple games, etc.