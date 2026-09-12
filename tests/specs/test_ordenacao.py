from tests.transactions.authentication import LoginTransaction
from tests.transactions.shopping import ShoppingTransaction


def test_ordenar_produtos_por_preco_decrescente(driver):
    LoginTransaction().run(driver)
    shopping = ShoppingTransaction(driver)
    shopping.sort_products_by("hilo")

    prices = shopping.product_prices()

    assert prices == sorted(prices, reverse=True)