from tests.pages.menu_page import MenuPage


class SessionTransaction:
    def __init__(self, driver):
        self.menu_page = MenuPage(driver)

    def logout(self):
        self.menu_page.open()
        self.menu_page.logout()

    def reset_app(self):
        self.menu_page.open()
        self.menu_page.reset_app_state()