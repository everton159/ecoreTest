from selenium.webdriver.common.by import By

class InvoiceLocators:
    INVOICE_LIST_TITLE = (By.XPATH, "//h2[contains(text(), 'Invoice List')]")
    FIRST_INVOICE_LINK = (By.XPATH, "//a[contains(text(), 'Invoice Details')][1]")
    INVOICE_DETAILS_TITLE = (By.XPATH, "//h2[contains(text(), 'Invoice Details')]")
    HOTEL_NAME = (By.XPATH, "//h4[@class='mt-5']")
    INVOICE_NUMBER = (By.XPATH, "//h6[@class='mt-2']")
    INVOICE_DATE = (By.XPATH, "//div/ul/li[1]")
    DUE_DATE = (By.XPATH, "//div/ul/li[2]")
    BOOKING_CODE = (By.XPATH, "//table[1]/tbody/tr[1]/td[2]")
    ROOM = (By.XPATH, "//table[@class='table']//tr[td[text()='Room']]/td[2]")
    TOTAL_STAY_COUNT = (By.XPATH, "//table[@class='table']//tr[td[text()='Total Stay Count']]/td[2]")
    TOTAL_STAY_AMOUNT = (By.XPATH, "//table[@class='table']//tr[td[text()='Total Stay Amount']]/td[2]")
    CHECK_IN = (By.XPATH, "//table[@class='table']//tr[td[text()='Check-In']]/td[2]")
    CHECK_OUT = (By.XPATH, "//table[@class='table']//tr[td[text()='Check-Out']]/td[2]")
    CUSTOMER_DETAILS = (By.XPATH, "//h5[contains(text(), 'Customer Details')]/following-sibling::div")
    DEPOSIT_NOW = (By.XPATH, "//div/table[2]/tbody/tr/td[1]")
    TAX_AND_VAT = (By.XPATH, "//div/table[2]/tbody/tr/td[2]")
    TOTAL_AMOUNT = (By.XPATH, "//table[@class='table']/tbody/tr/td[3]")

