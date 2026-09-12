import pytest

from tests.pages.inventory_page import InventoryPage
from tests.transactions.authentication import LoginTransaction


@pytest.mark.smoke
def test_login_saucedemo_sucesso(driver):
    LoginTransaction(driver).login()

    assert "inventory.html" in driver.current_url
    assert InventoryPage(driver).is_loaded()
