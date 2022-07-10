from selenium.webdriver.common.by import By

from PageObject.PlaceOrder import PlaceOrder
# oiegoihrgis

class HomePage:
    # self.driver.find_element(By.CSS_SELECTOR, "input.search-keyword")
    # self.driver.find_elements(By.XPATH, "//button[text()='ADD TO CART']")
    # self.driver.find_element(By.XPATH, "//div[@class='cart']/a/img").click()
    # self.driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")

    searchtext = (By.CSS_SELECTOR, "input.search-keyword")
    selectitem = (By.XPATH, "//button[text()='ADD TO CART']")
    cartbutton = (By.XPATH, "//div[@class='cart']/a/img")
    proceed_to_checkout= (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")

    def __init__(self, driver):
        self.driver = driver

    def searchbar(self):
        return self.driver.find_element(*HomePage.searchtext)
    def addcartitem(self):
        return self.driver.find_elements(*HomePage.selectitem)
    def cartbuttonclick(self):
        return self.driver.find_element(*HomePage.cartbutton)
    def checkoutbutton(self):
        self.driver.find_element(*HomePage.proceed_to_checkout).click()
        placeorder = PlaceOrder(self.driver)
        return placeorder
