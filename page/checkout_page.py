from selenium.webdriver.common.by import By
from base.base_page import BasePage

class CheckoutPage(BasePage):
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")

    def fill_info(self, firstname, lastname, postal):
        self.send_keys(self.first_name, firstname)
        self.send_keys(self.last_name, lastname)
        self.send_keys(self.postal_code, postal)
        self.click(self.continue_btn)