from selenium.webdriver.common.by import By


class PlaceOrder():
    # self.driver.find_element(By.CLASS_NAME, "promoCode")
    # self.driver.find_element(By.XPATH, "//button[text()='Apply']")
    # self.driver.find_element(By.XPATH, "//span[text()='Code applied ..!']")
    # self.driver.find_element(By.XPATH, "//span[text()='349.2']")
    # self.driver.find_element(By.XPATH, "//button[text()='Place Order']")

    orderpage = (By.CLASS_NAME, "promoCode")
    sendkeys = (By.XPATH, "//button[text()='Apply']")
    promotext = (By.XPATH, "//span[text()='Code applied ..!']")
    checkamount = (By.XPATH, "//span[text()='349.2']")
    placeorder = (By.XPATH, "//button[text()='Place Order']")

    def __init__(self, driver):
        self.driver = driver

    def placeorderpage(self):
        return self.driver.find_element(*PlaceOrder.orderpage)

    def promosendkeys(self):
        return self.driver.find_element(*PlaceOrder.sendkeys)

    def textpromotext(self):
        return self.driver.find_element(*PlaceOrder.promotext)

    def amountcheck(self):
        return self.driver.find_element(*PlaceOrder.checkamount)

    def clickorder(self):
        return self.driver.find_element(*PlaceOrder.placeorder)