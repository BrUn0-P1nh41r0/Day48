from selenium import webdriver

#Keep Chrome browser open aafer program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com")

driver.quit()