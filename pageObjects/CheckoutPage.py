from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage():
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    productName = (By.XPATH, "div/h4/a")
    selectProduct = (By.CSS_SELECTOR, "button[class*='btn']")
    checkoutBtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkoutBtn2 = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getProductName(self):
        return self.driver.find_element(*CheckOutPage.productName)

    def getProdcutSelect(self):
        return self.driver.find_element(*CheckOutPage.selectProduct)

    def pressCheckOut(self):
        return self.driver.find_element(*CheckOutPage.checkoutBtn)

    def pressCheckOutFinal(self):
        self.driver.find_element(*CheckOutPage.checkoutBtn2).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage
    
    
