import pytest
from selenium.webdriver.support.select import Select
from selenium import webdriver
from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.select import Select


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        homePage = HomePage(self.driver)
        homePage.inputName().send_keys(getData["firstname"])
        homePage.inputEmail().send_keys(getData["email"])
        homePage.tickCheck()
        self.selectOptionByText(homePage.selectGender(), getData["gender"])
        homePage.Submit().click()
        message = homePage.getMessage().text

        assert "success" in message

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param
