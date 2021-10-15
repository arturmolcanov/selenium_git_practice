from selenium.webdriver.common.by import By


class ConfirmPage():
    def __init__(self, driver):
        self.driver = driver
    
    dropdown = (By.CSS_SELECTOR, "input[id*='country']")
    dropdownselect = (By.LINK_TEXT, "Lithuania")
    checkbox = (By.CSS_SELECTOR, "div[class*='checkbox']")
    confirm = (By.CSS_SELECTOR, "input[class*='btn-success']")
    message = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def getDropdown(self):
        return self.driver.find_element(*ConfirmPage.dropdown)
    
    def selectFromDropdown(self):
        return self.driver.find_element(*ConfirmPage.dropdownselect)
    
    def tickCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def pressConfirm(self):
        return self.driver.find_element(*ConfirmPage.confirm)
    
    def getConfirmMessage(self):
        return self.driver.find_element(*ConfirmPage.message)