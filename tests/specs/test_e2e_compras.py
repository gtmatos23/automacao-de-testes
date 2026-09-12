from tests.transactions.authentication import LoginTransaction
from tests.transactions.checkout import CheckoutTransaction
from tests.transactions.shopping import ShoppingTransaction


def test_compra_com_multiplos_itens_valida_subtotal(driver):
    LoginTransaction().run(driver)
    shopping = ShoppingTransaction(driver)
    shopping.add_products(
        ["sauce-labs-backpack", "sauce-labs-bike-light", "sauce-labs-bolt-t-shirt"]
    )
    shopping.open_cart()
    expected_subtotal = sum(shopping.cart_item_prices())

    checkout = CheckoutTransaction(driver)
    checkout.run()
    checkout.fill_form("Alessandro", "QA", "12345")
    checkout.continue_checkout()

    assert checkout.subtotal() == expected_subtotal