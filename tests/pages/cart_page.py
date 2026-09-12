from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage


class CartPage(BasePage):

    CHECKOUT = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[id^='remove-']")

    def start_checkout(self):
        self.click(*self.CHECKOUT)

    def continue_shopping(self):
        self.click(*self.CONTINUE_SHOPPING)

    def get_item_count(self):
        return len(self.find_all(*self.ITEMS))

    def get_item_prices(self):
        def read_prices(driver):
            try:
                items = driver.find_elements(*self.ITEM_PRICES)
                if not items:
                    return False
                return [float(item.text.replace("$", "")) for item in items]
            except StaleElementReferenceException:
                return False

        return WebDriverWait(self.driver, self.TIMEOUT).until(read_prices)

    def remove_first_item(self):
        self.find_all(*self.REMOVE_BUTTONS)[0].click()
