from tests.fixtures.driver import create_driver
from tests.config.settings import Settings


def before_all(context):
    context.settings = Settings()


def before_scenario(context, scenario):
    context.driver = create_driver()


def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()