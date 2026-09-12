from tests.transactions.authentication import LoginTransaction
from tests.transactions.shopping import ShoppingTransaction


def test_ordenar_produtos_por_preco_crescente(driver):
    LoginTransaction(driver).login()
    shopping = ShoppingTransaction(driver)
    shopping.sort_products_by("lohi")

    prices = shopping.product_prices()
    assert prices == sorted(prices)


def test_ordenar_produtos_por_nome(driver):
    LoginTransaction(driver).login()
    shopping = ShoppingTransaction(driver)
    shopping.sort_products_by("az")

    names = shopping.product_names()
    assert names == sorted(names)
