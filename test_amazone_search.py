import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get('http://amazone.com/')
search = driver.find_element(By.ID,'twotabsearchtextbox')
search.send_keys('dress',Keys.ENTER)
time.sleep(5)
expected_text = '"dress"'
actual_text = driver.find_element(By.XPATH,"//span[@class='a-color-state a-text-bold']").text
assert expected_text == actual_text, f'Error. Expected text{expected_text}, but actual text: {actual_text}'
driver.quit()

