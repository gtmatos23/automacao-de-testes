from tests.pages.cart_page import CartPage
from tests.transactions.authentication import LoginTransaction
from tests.transactions.shopping import ShoppingTransaction


def test_acessar_carrinho_sem_itens(driver):
    LoginTransaction(driver).login()
    shopping = ShoppingTransaction(driver)
    shopping.open_cart()

    assert "cart.html" in driver.current_url
    assert CartPage(driver).get_item_count() == 0
