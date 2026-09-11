from tests.transactions.authentication import LoginTransaction
from tests.transactions.session import SessionTransaction
from tests.transactions.shopping import ShoppingTransaction


def test_resetar_carrinho(driver):
    LoginTransaction(driver).login()
    shopping = ShoppingTransaction(driver)
    shopping.add_backpack()
    assert shopping.cart_badge_count() == 1

    SessionTransaction(driver).reset_app()

    assert shopping.cart_badge_count() == 0