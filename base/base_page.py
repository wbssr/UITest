from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.find(locator).click()

    def send_keys(self, locator, text):
        self.find(locator).send_keys(text)

    def get_title(self):
        return self.driver.title

    # 失败截图
    def save_screenshot(self, name):
        if not os.path.exists("screenshot"):
            os.mkdir("screenshot")
        self.driver.save_screenshot(f"screenshot/{name}.png")