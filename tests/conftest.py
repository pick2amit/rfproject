import pytest
from selenium import webdriver
from base.web_driver_factory import WebDriverFactory

@pytest.yield_fixture()
def setUp():
    print()
    yield
    print()

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    wdf = WebDriverFactory(browser, osType)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", help="Type of browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")


