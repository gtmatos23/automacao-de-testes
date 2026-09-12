from selenium.webdriver.common.by import By
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
        return [
            float(item.text.replace("$", ""))
            for item in self.find_all(*self.ITEM_PRICES)
        ]

    def remove_first_item(self):
        self.find_all(*self.REMOVE_BUTTONS)[0].click()
