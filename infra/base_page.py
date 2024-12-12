from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class BasePage:
    BASE_URL = "https://automation-sandbox-python-mpywqjbdza-uc.a.run.app"
    DEFAULT_TIMEOUT = 30


    def __init__(self, driver, timeout=None):
        self.driver = driver
        self.timeout = timeout if timeout else self.DEFAULT_TIMEOUT
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(self.__class__.__name__)

    def go_to(self, endpoint=""):
        """Navigate to a specific endpoint of the base URL"""
        full_url = f"{self.BASE_URL}/{endpoint}".strip("/")
        self.logger.info(f"Navigating to URL: {full_url}")
        self.driver.get(full_url)

    def find_element(self, locator):
        self.logger.info(f"Finding element: {locator}")
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.logger.info(f"Clicking element: {locator}")
        self.find_element(locator).click()

    def type_text(self, locator, text):
        self.logger.info(f"Typing text '{text}' into element: {locator}")
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
