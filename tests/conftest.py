import pytest

@pytest.fixture
def url():
    return 'https://www.saucedemo.com/'

@pytest.fixture
def items_url():
    return 'https://www.saucedemo.com/inventory.html'

@pytest.fixture
def no_input_error_message():
    return 'Epic sadface: Username is required'
