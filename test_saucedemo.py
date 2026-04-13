import time

import pytest
from selenium import webdriver
from page.login_page import LoginPage
from page.product_page import ProductPage
from page.cart_page import CartPage
from selenium.webdriver.chrome.service import Service
from page.checkout_page import CheckoutPage
from page.order_page import OrderPage

@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome(
        service=Service(r"D:\pythonProject\WebAutoTest\chromedriver.exe")
    )
    driver.maximize_window()
    yield driver
    driver.quit()

# 参数化：多个用户测试
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
])

class TestSauceDemoFullFlow:
    def test_full_buy_process(self, driver,username,password):
        try:
            # 1. 登录
            login = LoginPage(driver)
            login.login(username, password)

            # 2. 加购商品
            product = ProductPage(driver)
            product.add_first_product_to_cart()
            product.go_to_cart()

            # 3. 去结算
            cart = CartPage(driver)
            cart.go_to_checkout()

            # 4. 填写信息
            checkout = CheckoutPage(driver)
            checkout.fill_info("Zhang", "San", "100000")

            # 5. 完成订单
            order = OrderPage(driver)
            order.finish_order()

            # 断言成功
            success_text = order.get_success_text()
            assert "Thank you" in success_text
            print(f"✅ 用户【{username}】流程全部成功")


        except Exception as e:
            #失败自动截图
            login.save_screenshot(f"失败_{username}")
            raise e

class TestSauceDemoAbnormal:
    """异常场景测试"""

    def test_login_fail_wrong_password(self, driver):
        login = LoginPage(driver)

        try:
            login.login("standard_user", "wrong_password")

            # 断言：登录失败，URL 不变
            assert "inventory" not in driver.current_url

            # 断言：显示错误提示
            from selenium.webdriver.common.by import By
            error_msg = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
            assert "Username and password do not match" in error_msg

            print("✅ 错误密码登录测试通过")

        except Exception as e:
            # 失败时截图
            login.save_screenshot("异常_错误密码登录")
            raise e