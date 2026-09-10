# base_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver

    def find(self, by, value):
        locator = (by, value)
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.presence_of_element_located(locator)
        )

    def find_all(self, by, value):
        return self.driver.find_elements(by, value)

    def click(self, by, value):
        locator = (by, value)
        WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def type(self, by, value, text):
        self.find(by, value).send_keys(text)

    def get_text(self, by, value):
        return self.find(by, value).text

    def is_displayed(self, by, value):
        return self.find(by, value).is_displayed()
