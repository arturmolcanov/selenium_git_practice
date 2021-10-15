from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    check = (By.ID ,"exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    message = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage
    
    def inputName(self):
        return self.driver.find_element(*HomePage.name)
    
    def inputEmail(self):
        return self.driver.find_element(*HomePage.email)
    
    def tickCheck(self):
        return self.driver.find_element(*HomePage.check)
    
    def selectGender(self):
        return self.driver.find_element(*HomePage.gender)
    
    def Submit(self):
        return self.driver.find_element(*HomePage.submit)

    def getMessage(self):
        return self.driver.find_element(*HomePage.message)
