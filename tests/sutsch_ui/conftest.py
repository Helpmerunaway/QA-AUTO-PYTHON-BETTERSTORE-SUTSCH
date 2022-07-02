import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from .pages.locators import ForgotPasswordPageLocators
from tests.sutsch_ui.pages.login_page import LoginPageLocators
from .pages.login_page import MainPageLocators
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from tests.sutsch_ui.config import STAGE_LOGIN_USER_2, STAGE_PASSWORD_USER_2, STAGE_AUTH_URL, STAGE_LOGIN_USER_1, \
    GH_TOKEN
import os
import logging


os.environ['WDM_LOG'] = "false"

os.environ['GH_TOKEN'] = GH_TOKEN


logging.getLogger('WDM').setLevel(logging.NOTSET)


def pytest_addoption(parser):
    """Declaring the command-line options for test run"""
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome, edge or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: en, ru, es etc.")
    parser.addoption('--headless',
                     default='true',
                     help='headless options: "true" or "false"')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption('--headless')
    chrome_option = webdriver.ChromeOptions()
    firefox_option = webdriver.FirefoxOptions()
    edge_option = webdriver.EdgeOptions()
    if browser_name == "chrome":
        if headless == 'true':
            chrome_option.add_argument('--headless')
            chrome_option.add_argument('--ignore-certificate-errors')
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
    elif browser_name == "firefox":
        if headless == 'true':
            firefox_option.add_argument('--headless')
            firefox_option.add_argument('--ignore-certificate-errors')
        browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_option)
    elif browser_name == 'edge':
        if headless == 'true':
            edge_option.add_argument('--headless')
            edge_option.add_argument('--ignore-certificate-errors')
        browser = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_option)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()


@pytest.fixture()
def test_auth_ui(browser):
    print("Start Authorisation")
    browser.get(STAGE_AUTH_URL)
    input_email_user_2 = browser.find_element(*LoginPageLocators.LOGIN_EMAIL_INPUT)
    input_email_user_2.click()
    input_email_user_2.clear()
    input_email_user_2.send_keys(STAGE_LOGIN_USER_2)
    input_password_user_2 = browser.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT)
    input_password_user_2.click()
    input_password_user_2.clear()
    input_password_user_2.send_keys(STAGE_PASSWORD_USER_2)
    enter_button = browser.find_element(*LoginPageLocators.ENTER_STAGE_BUTTON)
    enter_button.click()
    yield
    logout_button = browser.find_element(*MainPageLocators.EXIT_USER_BUTTON)
    ActionChains(browser).move_to_element(logout_button).click().perform()
    print('End Authorization')


@pytest.fixture()
def reset_password_ui_link_to_email(browser):
    print("Working on reset request")
    browser.get(STAGE_AUTH_URL)
    forgot_password_button = browser.find_element(*LoginPageLocators.FORGOT_PASSWORD_BUTTON)
    forgot_password_button.click()
    enter_email = browser.find_element(*ForgotPasswordPageLocators.EMAIL_INPUT)
    enter_email.click()
    enter_email.clear()
    enter_email.send_keys(STAGE_LOGIN_USER_1)
    reset_password = browser.find_element(*ForgotPasswordPageLocators.RESET_PASSWORD_BUTTON)
    reset_password.click()


