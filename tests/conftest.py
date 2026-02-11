import pytest
from playwright.sync_api import Playwright, BrowserContext

@pytest.fixture(autouse=True, scope='session')
def playwright_settings(playwright: Playwright):
    playwright.selectors.set_test_id_attribute('data-test')
    return playwright

@pytest.fixture
def auth_context(context: BrowserContext):
    context.add_cookies([{
        'name': 'session-username',
        'value': 'standard_user',
        'domain': 'www.saucedemo.com',
        'path': '/'
    }])

    return context

@pytest.fixture
def shop_url():
    return 'https://www.saucedemo.com/'

@pytest.fixture
def products_url():
    return 'https://www.saucedemo.com/inventory.html'

@pytest.fixture
def cart_url():
    return 'https://www.saucedemo.com/cart.html'
