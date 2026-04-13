from selenium.webdriver.common.by import By
from base.base_page import BasePage

class OrderPage(BasePage):
    finish_btn = (By.ID, "finish")
    success_msg = (By.CLASS_NAME, "complete-header")

    def finish_order(self):
        self.click(self.finish_btn)

    def get_success_text(self):
        return self.find(self.success_msg).text