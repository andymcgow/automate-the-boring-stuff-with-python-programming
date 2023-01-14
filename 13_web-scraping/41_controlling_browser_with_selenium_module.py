from selenium import webdriver

browser = webdriver.Safari()
browser.get("https://automatetheboringstuff.com")
elem = browser.find_elements_by_css_selector("body > div > main > div > ul:nth-child(19) > li:nth-child(1) > a")
elem.click()

# .send_keys() - Use this to send text to search or input fields.
# browser.back() - Go back a page in the browser
# browser.forward() - Go forward a page in the browser
# browser.refresh() - Refresh the browser
# browser.quit() - Quite the browser
