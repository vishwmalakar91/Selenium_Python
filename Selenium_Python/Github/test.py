from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\vmalakar\Downloads\\chromedriver.exe")
driver.maximize_window()
driver.get("https://github.com")
driver.implicitly_wait(200)
print(driver.title)
assert "The world’s leading software development platform · GitHub" in driver.title
driver.get_screenshot_as_file("github.png")
driver.close()