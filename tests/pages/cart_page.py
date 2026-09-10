from selenium.webdriver.common.by import By
from .base_page import BasePage


class CartPage(BasePage):

    CHECKOUT = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    ITEMS = (By.CLASS_NAME, "cart_item")

    def start_checkout(self):
        self.click(*self.CHECKOUT)

    def continue_shopping(self):
        self.click(*self.CONTINUE_SHOPPING)

    def get_item_count(self):
        return len(self.find_all(*self.ITEMS))
