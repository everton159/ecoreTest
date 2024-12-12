import unittest
from infra.driver_factory import DriverFactory
from pages.login_page import LoginPage
from pages.invoice_page import InvoicePage
from locators.invoice_locators import InvoiceLocators

class TestInvoice(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverFactory.create_driver()
        cls.login_page = LoginPage(cls.driver)
        cls.invoice_page = InvoicePage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.login_page.go_to()
        self.login_page.login("demouser", "abc123")

    def test_invoice_details_validation(self):
        self.invoice_page.click_first_invoice_details()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.assertTrue(self.invoice_page.validate_invoice_details_page())

        expected_data = {
            InvoiceLocators.HOTEL_NAME: "Rendezvous Hotel",
            InvoiceLocators.INVOICE_NUMBER: "Invoice #110 details",
            InvoiceLocators.INVOICE_DATE: "Invoice Date: 14/01/2018",
            InvoiceLocators.DUE_DATE: "Due Date: 15/01/2018",
            InvoiceLocators.BOOKING_CODE: "0875",
            InvoiceLocators.ROOM: "Superior Double",
            InvoiceLocators.TOTAL_STAY_COUNT: "1",
            InvoiceLocators.TOTAL_STAY_AMOUNT: "$150",
            InvoiceLocators.CHECK_IN: "14/01/2018",
            InvoiceLocators.CHECK_OUT: "15/01/2018",
            InvoiceLocators.CUSTOMER_DETAILS: "JOHNY SMITH\nR2, AVENUE DU MAROC\n123456",
            InvoiceLocators.DEPOSIT_NOW: "USD $20.90",
            InvoiceLocators.TAX_AND_VAT: "USD $19",
            InvoiceLocators.TOTAL_AMOUNT: "USD $209",
        }

        for locator, expected_value in expected_data.items():
            with self.subTest(locator=locator):
                actual_value = self.invoice_page.get_field_value(locator)
                self.assertEqual(actual_value, expected_value)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
