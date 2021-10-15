import pytest
from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions
#from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif browser_name == "IE":
        pass
    elif browser_name == "firefox":
        pass

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
