from selenium.webdriver.common.by import By
from base.base_page import BasePage

class ProductPage(BasePage):
    # 商品名称 + 加入购物车按钮（以第一个商品为例）
    first_product = (By.XPATH, "//div[text()='Sauce Labs Backpack']")
    add_to_cart_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    # 添加商品到购物车
    def add_first_product_to_cart(self):
        self.click(self.add_to_cart_btn)

    # 进入购物车
    def go_to_cart(self):
        self.click(self.cart_icon)