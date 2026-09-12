from tests.pages.inventory_page import InventoryPage
from tests.transactions.authentication import LoginTransaction
from tests.transactions.shopping import ShoppingTransaction


def test_continuar_comprando_apos_adicionar_item(driver):
    LoginTransaction(driver).login()
    shopping = ShoppingTransaction(driver)
    shopping.add_backpack()
    shopping.open_cart()
    shopping.continue_shopping()

    assert "inventory.html" in driver.current_url
    assert InventoryPage(driver).get_product_count() > 0
