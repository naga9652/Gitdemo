from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions, wait
from selenium.webdriver.support.wait import WebDriverWait


class webdriverwit():
    def __init__(self, locator, text):
        self.locator = locator
        self.text = text
    def waitpromocode(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_element_located((self.locator, self.text)))
