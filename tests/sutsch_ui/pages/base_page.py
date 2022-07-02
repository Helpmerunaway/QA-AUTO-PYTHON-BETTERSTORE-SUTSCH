from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from tests.sutsch_ui.pages import locators

browser: WebDriver = ...
timeout: int = 4


class BasePage():

    locator = locators

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.browser.maximize_window()
        self.url = url
        self.browser.implicitly_wait(timeout)

    def wait(self):
        return WebDriverWait(browser, timeout=timeout, ignored_exceptions=(WebDriverException,))

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def action_chains(self):
        return ActionChains(self.browser)

    def scroll_to(self, locator):
        self.browser.execute_script('arguments[0].scrollIntoView(true);', locator)

    def exec_script(self):
        element = self.browser.find_element_by_css("//i[contains(@class, 'delete')]")
        self.browser.execute_script("arguments[0].click();", element)

    def find(self, locator, wait=3):
        """
        Нахождение элементов
        """
        return WebDriverWait(self.browser, wait).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")
