import pytest
from playwright.sync_api import Page, expect

def test_success_login(page: Page):
    page.goto('https://www.saucedemo.com/')
    page.locator('id=user-name').fill('standard_user')
    page.locator('id=password').fill('secret_sauce')
    page.locator('id=login-button').click()
    page.wait_for_timeout(5000.0)


def test_empty_fields(page: Page):
    page.goto('https://www.saucedemo.com/')
    page.locator('id=login-button').click()
    page.wait_for_timeout(5000.0)