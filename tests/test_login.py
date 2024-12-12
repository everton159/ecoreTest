import unittest
from infra.driver_factory import DriverFactory
from pages.login_page import LoginPage

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverFactory.create_driver()
        cls.login_page = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.login_page.go_to()

    def test_login_positive(self):
        self.login_page.login("demouser", "abc123")
        self.assertIn("Invoice List", self.driver.page_source)

    def test_login_negative(self):
        invalid_credentials = [
            ("demouser", "wrongpassword"),
            ("invaliduser", "abc123"),
            ("", "abc123"),
            ("demouser", ""),
        ]
        for username, password in invalid_credentials:
            with self.subTest(username=username, password=password):
                self.login_page.login(username, password)
                error_message = self.login_page.get_error_message()
                self.assertEqual(error_message, "Wrong username or password.")
