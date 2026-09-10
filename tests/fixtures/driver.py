from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import tempfile


@pytest.fixture
def driver():
    driver = create_driver()

    yield driver

    driver.quit()


def create_driver():
    chrome_options = Options()

    # Perfil limpo e isolado
    user_data_dir = tempfile.mkdtemp()
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

    # Desativa Password Manager
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    }

    chrome_options.add_experimental_option("prefs", prefs)

    # Desativa detecção de vazamento
    chrome_options.add_argument("--disable-features=PasswordLeakDetection")
    chrome_options.add_argument("--safebrowsing-disable-leak-detection")

    # Configurações adicionais
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()

    return driver


# Mantém compatibilidade com código que já utilizava driver_func()
def driver_func():
    return create_driver()