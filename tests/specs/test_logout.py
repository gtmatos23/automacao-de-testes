from tests.pages.login_page import LoginPage
from tests.transactions.authentication import LoginTransaction
from tests.transactions.session import SessionTransaction


def test_logout_com_sucesso(driver):
    LoginTransaction(driver).login()
    SessionTransaction(driver).logout()

    assert "saucedemo.com" in driver.current_url
    assert LoginPage(driver).is_login_button_displayed()
