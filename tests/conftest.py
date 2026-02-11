import pytest
from playwright.sync_api import Playwright

@pytest.fixture(autouse=True, scope='session')
def playwright_settings(playwright: Playwright):
    playwright.selectors.set_test_id_attribute('data-test')
    return playwright

@pytest.fixture
def base_url():
    return 'https://www.saucedemo.com/'

@pytest.fixture
def items_url():
    return 'https://www.saucedemo.com/inventory.html'

@pytest.fixture
def cart_url():
    return 'https://www.saucedemo.com/cart.html'

@pytest.fixture
def no_input_error_message():
    return 'Epic sadface: Username is required'

@pytest.fixture
def wrong_input_error_message():
    return 'Epic sadface: Username and password do not match any user in this service'
