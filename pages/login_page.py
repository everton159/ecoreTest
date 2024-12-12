from infra.base_page import BasePage
from locators.login_locators import LoginLocators

class LoginPage(BasePage):
    def login(self, username, password):
        self.type_text(LoginLocators.USERNAME, username)
        self.type_text(LoginLocators.PASSWORD, password)
        self.click(LoginLocators.LOGIN_BUTTON)

    def get_error_message(self):
        return self.find_element(LoginLocators.ERROR_MESSAGE).text
