from selenium.webdriver.common.by import By

from .base_page import BasePage


class MenuPage(BasePage):

    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT = (By.ID, "logout_sidebar_link")
    RESET_APP_STATE = (By.ID, "reset_sidebar_link")

    def open(self):
        self.click(*self.MENU_BUTTON)

    def logout(self):
        self.click(*self.LOGOUT)

    def reset_app_state(self):
        self.click(*self.RESET_APP_STATE)
