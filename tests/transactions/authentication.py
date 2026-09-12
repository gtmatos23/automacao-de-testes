from tests.pages.login_page import LoginPage


class LoginTransaction:
    def __init__(self, driver=None, username="standard_user", password="secret_sauce"):
        self.driver = driver
        self.username = username
        self.password = password
        self.login_page = LoginPage(driver) if driver else None

    def run(self, driver=None):
        driver = driver or self.driver
        self.login_page = LoginPage(driver)
        self.login_page.open()
        self.login_page.login(self.username, self.password)
        return driver.current_url

    def login(self, username="standard_user", password="secret_sauce"):
        self.username = username
        self.password = password
        return self.run()
