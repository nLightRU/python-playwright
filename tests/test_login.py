import pytest
import playwright
from playwright.sync_api import Page, expect

# To Do: Check placeholder

@pytest.mark.smoke
@pytest.mark.login
def test_success_login(page: Page):
    page.goto('https://www.saucedemo.com/')
    page.locator('id=user-name').fill('standard_user')
    page.locator('id=password').fill('secret_sauce')
    page.locator('id=login-button').click()
    page.wait_for_timeout(5000.0)


@pytest.mark.skip
def test_success_login_by_test_id(page: Page):
    playwright.selectors.set_test_id_attribute('data-test')
    page.goto('https://www.saucedemo.com/')
    page.get_by_test_id('username').fill('standard_user')
    page.get_by_test_id('password').fill('secret_sauce')
    page.get_by_test_id('login-button').click()
    page.wait_for_timeout(5000.0)


@pytest.mark.login
def test_empty_fields(page: Page):
    page.goto('https://www.saucedemo.com/')
    page.locator('id=login-button').click()
    page.wait_for_timeout(5000.0)