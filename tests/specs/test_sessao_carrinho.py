from tests.pages.login_page import LoginPage
from tests.transactions.authentication import LoginTransaction
from tests.transactions.session import SessionTransaction
from tests.transactions.shopping import ShoppingTransaction


def test_contador_do_carrinho_persiste_apos_logout_e_relogin(driver):
    LoginTransaction().run(driver)
    shopping = ShoppingTransaction(driver)
    shopping.add_products(["sauce-labs-backpack", "sauce-labs-bike-light"])
    assert shopping.cart_badge_count() == 2

    shopping.open_cart()
    shopping.remove_first_cart_item()
    shopping.continue_shopping()
    assert shopping.cart_badge_count() == 1

    SessionTransaction(driver).run()
    assert LoginPage(driver).is_login_button_displayed()

    LoginTransaction().run(driver)
    assert ShoppingTransaction(driver).cart_badge_count() == 1