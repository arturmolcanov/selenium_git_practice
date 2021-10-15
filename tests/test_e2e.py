import pytest
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkOutPage = homepage.shopItems()
        products = checkOutPage.getCardTitles()
        log.info("Got product titles")
        for product in products:
            productName = product.text
            if productName == "Blackberry":
                checkOutPage.getProdcutSelect().click()
        
        log.info("Got blackberry phone")

        checkOutPage.pressCheckOut().click()
        confirmPage = checkOutPage.pressCheckOutFinal()
        confirmPage.getDropdown().send_keys("Lith")
        self.verifyLinkPresence("Lithuania")
        confirmPage.selectFromDropdown().click()
        confirmPage.tickCheckbox().click()
        confirmPage.pressConfirm().click()
        message = confirmPage.getConfirmMessage().text
        log.info("Got message")

        assert "Success! Thank you!" in message
