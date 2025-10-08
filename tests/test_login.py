import pytest
from playwright.sync_api import Playwright, Page, expect

# To Do: Check placeholder

@pytest.mark.smoke
@pytest.mark.login
def test_success_login(page: Page):
    page.goto('https://www.saucedemo.com/')
    page.locator('id=user-name').fill('standard_user')
    page.locator('id=password').fill('secret_sauce')
    page.locator('id=login-button').click()
    page.wait_for_timeout(5000.0)
    expect(page.locator('.inventory_list')).to_be_visible()


@pytest.mark.login
def test_success_login_by_test_id(playwright: Playwright, page: Page):
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
    expect(page.locator('.error-message-container')).to_be_visible()
    