from tests.pages.login_page import LoginPage


class LoginTransaction:
    def __init__(self, driver):
        self.login_page = LoginPage(driver)

    def login(self, username="standard_user", password="secret_sauce"):
        self.login_page.open()
        self.login_page.login(username, password)
        return self.login_page.driver.current_url