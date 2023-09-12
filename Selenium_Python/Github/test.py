from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://github.com")
driver.implicitly_wait(200)
print("Title is - " + driver.title)
assert "GitHub: Let’s build from here · GitHub" in driver.title
driver.get_screenshot_as_file("github.png")
driver.close()
