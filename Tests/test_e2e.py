import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from PageObject.HomePage import HomePage
from PageObject.Proceedfile import ProceedPage
from Utilities.BaseClass import baseclass
from Utilities.promocodewait import webdriverwit

i hate to complete the things whatever the situation 

class Testone(baseclass):
    def test_e2eone(self):
        homepage = HomePage(self.driver)
        homepage.searchbar().send_keys("ber")
        time.sleep(2)
        buttons = homepage.addcartitem()
        for button in buttons:
#             button.click()
#         homepage.cartbuttonclick().click()
#         placeorder = homepage.checkoutbutton()
#         WAITDEM = webdriverwit.waitpromocode(self.locator, "promocode")
#         placeorder.placeorderpage().send_keys("rahulshettyacademy")
#         placeorder.promosendkeys().click()
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
#         promo_code = placeorder.textpromotext().text
#         print(promo_code)
#         assert "Code" in promo_code
#         total_amount = placeorder.amountcheck().text
#         print(total_amount)
#         assert total_amount == "349.2"
#         placeorder.clickorder().click()
#         proceed = ProceedPage(self.driver)
#         sel = Select(proceed.country())
#         sel.select_by_index(2)
#         proceed.procedpagelast().click()
#         proceed.proceedbuttonpress().click()