from infra.base_page import BasePage
from locators.invoice_locators import InvoiceLocators

class InvoicePage(BasePage):
    def validate_invoice_list_page(self):
        return self.find_element(InvoiceLocators.INVOICE_LIST_TITLE)

    def click_first_invoice_details(self):
        self.click(InvoiceLocators.FIRST_INVOICE_LINK)

    def validate_invoice_details_page(self):
        return self.find_element(InvoiceLocators.INVOICE_DETAILS_TITLE)

    def get_field_value(self, locator):
        return self.find_element(locator).text

    def get_due_date(self):
        element = self.find_element(InvoiceLocators.DUE_DATE)
        return element.text.split(":")[1].strip()