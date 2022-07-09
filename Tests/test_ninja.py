import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Testninjaproject():

    def test_ninjapractice(self):
        time.sleep(5)
        driver = webdriver.Chrome("D:\\Driver\\chromedriver.exe")
        driver.get("http://tutorialsninja.com/demo/index.php?route=common/home")
        driver.maximize_window()
        # fistr click
        driver.find_element(By.LINK_TEXT, "Phones & PDAs").click()
        driver.find_element(By.XPATH, "//img[@title='iPhone']").click()
        driver.find_element(By.XPATH, "//ul/li[1]/a[1]/img[1]").click()
        right_button = driver.find_element(By.XPATH, "//button[@title='Next (Right arrow key)']")
        for i in range(0, 5):
            right_button.click()
        driver.save_screenshot("screenshot"+str(random.randint(0, 101))+".png")
        driver.find_element(By.XPATH, "//button[@title='Close (Esc)']").click()
        driver