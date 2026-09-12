import pytest

from tests.transactions.authentication import LoginTransaction
from tests.transactions.checkout import CheckoutTransaction
from tests.transactions.shopping import ShoppingTransaction


@pytest.fixture
def checkout(driver):
    LoginTransaction(driver).login()
    shopping = ShoppingTransaction(driver)
    shopping.add_backpack()
    shopping.open_cart()
    checkout_transaction = CheckoutTransaction(driver)
    checkout_transaction.start()
    return checkout_transaction


def test_checkout_sem_preencher_dados(checkout, driver):
    checkout.continue_without_data()

    assert "checkout-step-one.html" in driver.current_url
    assert "First Name is required" in checkout.error_message()


def test_checkout_parcial(checkout):
    checkout.fill_first_name("Gustavo")
    checkout.continue_without_data()

    assert "Last Name is required" in checkout.error_message()
