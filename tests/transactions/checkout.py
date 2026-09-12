from tests.pages.cart_page import CartPage
from tests.pages.checkout_page import CheckoutPage


class CheckoutTransaction:
    def __init__(self, driver):
        self.cart_page = CartPage(driver)
        self.checkout_page = CheckoutPage(driver)

    def run(self, driver=None):
        if driver:
            self.cart_page = CartPage(driver)
            self.checkout_page = CheckoutPage(driver)
        self.start()
        return self.checkout_page.driver.current_url

    def start(self):
        self.cart_page.start_checkout()

    def continue_without_data(self):
        self.checkout_page.continue_checkout()

    def continue_checkout(self):
        self.checkout_page.continue_checkout()

    def fill_first_name(self, name):
        self.checkout_page.fill_first_name(name)

    def error_message(self):
        return self.checkout_page.get_error_message()

    def fill_form(self, name, last, zip_code):
        self.checkout_page.fill_form(name, last, zip_code)

    def subtotal(self):
        return self.checkout_page.get_subtotal()