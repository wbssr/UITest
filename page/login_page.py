from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    # 元素定位
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_btn = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.saucedemo.com/")

    # 业务方法
    def login(self, username, password):
        self.send_keys(self.username_input, username)
        self.send_keys(self.password_input, password)
        self.click(self.login_btn)