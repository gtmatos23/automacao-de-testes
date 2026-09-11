import os
import pytest
from tests.fixtures.driver import create_driver

@pytest.fixture
def driver():
    driver_instance = create_driver()
    yield driver_instance
    driver_instance.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver_instance = item.funcargs.get("driver")
        if driver_instance:
            os.makedirs("reports/screenshots", exist_ok=True)
            screenshot_path = f"reports/screenshots/{item.name}.png"
            driver_instance.save_screenshot(screenshot_path)