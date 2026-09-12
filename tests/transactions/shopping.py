from tests.pages.cart_page import CartPage
from tests.pages.inventory_page import InventoryPage


class ShoppingTransaction:
    def __init__(self, driver):
        self.inventory_page = InventoryPage(driver)
        self.cart_page = CartPage(driver)

    def run(self, driver=None):
        if driver:
            self.inventory_page = InventoryPage(driver)
            self.cart_page = CartPage(driver)
        self.add_products(["sauce-labs-backpack"])
        return self.cart_badge_count()

    def add_backpack(self):
        self.inventory_page.add_product()

    def add_products(self, product_ids):
        for product_id in product_ids:
            self.inventory_page.add_product_by_id(product_id)

    def remove_product(self, product_id):
        self.inventory_page.remove_product_by_id(product_id)

    def remove_first_cart_item(self):
        self.cart_page.remove_first_item()

    def cart_item_prices(self):
        return self.cart_page.get_item_prices()

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
