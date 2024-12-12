from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME = (By.NAME, "username") 
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.ID, "btnLogin")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert alert-danger')]")
