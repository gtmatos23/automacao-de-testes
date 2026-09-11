from tests.pages.cart_page import CartPage
from tests.pages.inventory_page import InventoryPage


class ShoppingTransaction:
    def __init__(self, driver):
        self.inventory_page = InventoryPage(driver)
        self.cart_page = CartPage(driver)

    def add_backpack(self):
        self.inventory_page.add_product()

    def open_cart(self):
        self.inventory_page.go_to_cart()

    def continue_shopping(self):
        self.cart_page.continue_shopping()

    def cart_item_count(self):
        return self.cart_page.get_item_count()

    def product_count(self):
        return self.inventory_page.get_product_count()

    def cart_badge_count(self):
        return self.inventory_page.get_cart_badge_count()

    def sort_products_by(self, value):
        self.inventory_page.sort_by(value)

    def product_names(self):
        return self.inventory_page.get_product_names()

    def product_prices(self):
        return self.inventory_page.get_product_prices()