from selenium.webdriver.common.by import By


class ProceedPage():
    # self.driver.find_element(By.XPATH, "//select[@style='width: 200px;']")
    # self.driver.find_element(By.CLASS_NAME, "chkAgree")
    # self.driver.find_element(By.XPATH, "//button[text()='Proceed']")

    proceedpage = (By.CLASS_NAME, "chkAgree")
    countryselect = (By.XPATH, "//select[@style='width: 200px;']")
    proceedbutton = (By.XPATH, "//button[text()='Proceed']")

    def __init__(self, driver):
        self.driver = driver

    def procedpagelast(self):
        return self.driver.find_element(*ProceedPage.proceedpage)

    def country(self):
        return self.driver.find_element(*ProceedPage.countryselect)

    def proceedbuttonpress(self):
        return self.driver.find_element(*ProceedPage.proceedbutton)