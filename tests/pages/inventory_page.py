from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from .base_page import BasePage


class InventoryPage(BasePage):

    INVENTORY_CONTAINER = (By.ID, "inventory_container")

    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SORT = (By.CLASS_NAME, "product_sort_container")
    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")

    def _product_button(self, product_id, action):
        return By.ID, f"{action}-to-cart-{product_id}"

    def is_loaded(self):
        return self.is_displayed(*self.INVENTORY_CONTAINER)

    def add_product(self):
        self.click(*self.ADD_BACKPACK)

    def add_product_by_id(self, product_id):
        self.click(*self._product_button(product_id, "add"))

    def remove_product_by_id(self, product_id):
        self.click(*self._product_button(product_id, "remove"))

    def go_to_cart(self):
        self.click(*self.CART)

    def sort_by(self, value):
        Select(self.find(*self.SORT)).select_by_value(value)

    def get_product_count(self):
        return len(self.find_all(*self.PRODUCTS))

    def get_product_names(self):
        return [product.text for product in self.find_all(*self.PRODUCT_NAMES)]

    def get_product_prices(self):
        return [
            float(product.text.replace("$", ""))
            for product in self.find_all(*self.PRODUCT_PRICES)
        ]

    def get_cart_badge_count(self):
        badges = self.find_all(*self.CART_BADGE)
        return int(badges[0].text) if badges else 0