from selenium.webdriver.common.by import By
from base.base_page import BasePage

class CartPage(BasePage):
    # 去结算按钮
    checkout_btn = (By.ID, "checkout")

    def go_to_checkout(self):
        self.click(self.checkout_btn)