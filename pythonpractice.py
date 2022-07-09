import random
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
ser = Service("D:\\Driver\\chromedriver.exe")
driver = webdriver.Chrome(service=ser)
# driver = webdriver.Chrome("D:\\Driver\\chromedriver.exe")
driver.get("http://tutorialsninja.com/demo/index.php?route=common/home")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Phones & PDAs").click()
driver.find_element(By.XPATH, "//img[@title='iPhone']").click()
driver.find_element(By.XPATH, "//ul/li[1]/a[1]/img[1]").click()
rightclick = driver.find_element(By.XPATH, "//button[@title='Next (Right arrow key)']")
for i in range(1, 6):
    rightclick.click()
driver.save_screenshot("screenshot"+str(random.randint(0, 101))+".png")
driver.find_element(By.XPATH, "//button[@title='Close (Esc)']").click()
driver.find_element(By.ID, "input-quantity").clear()
driver.find_element(By.ID, "input-quantity").send_keys(2)
driver.find_element(By.ID, "button-cart").click()
time.sleep(3)
cost = driver.find_element(By.XPATH, "//span[@id='cart-total']").text
time.sleep(2)
print(cost)
driver.find_element(By.CSS_SELECTOR, "button[class*='btn-inverse']").click()
loptops = driver.find_element(By.XPATH, "//a[text()='Laptops & Notebooks']")
action = ActionChains(driver)
action.move_to_element(loptops).perform()
driver.find_element(By.XPATH, "//a[text()='Show All Laptops & Notebooks']").click()
time.sleep(3)
lopsec = driver.find_element(By.XPATH, "//h2[text()='Laptops & Notebooks']").text
print(lopsec)
driver.find_element(By.XPATH, "//a[text()='HP LP3065']").click()
loptop_button = driver.find_element(By.ID, "button-cart")
loptop_button.location_once_scrolled_into_view
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "i[class*='fa-calendar']").click()
calender_obj = driver.find_element(By.XPATH, "//th[@class='picker-switch']")
next_obj = driver.find_element(By.XPATH, "//th[@class='next']")
while calender_obj.text != "December 2022":
    next_obj.click()
date_obj = driver.find_element(By.XPATH, "//td[text()='31']")
date_obj.click()
driver.find_element(By.XPATH, "//button[text()='Add to Cart']").click( )
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "button[class*='btn-inverse'] span").click()
driver.find_element(By.XPATH, "//p[@class='text-right']/a[2]").click()
fail_text = driver.find_element(By.CSS_SELECTOR, "div[class*='alert-danger']").text
print(fail_text)

assert "are not available" in fail_text
driver.find_element(By.XPATH, "//tr[1]/td[5]/button[1]/i[1]").click()

C:\Users\Hi\PycharmProjects\pythonProject8