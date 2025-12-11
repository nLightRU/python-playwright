import pytest
from playwright.sync_api import Page, expect

@pytest.mark.smoke
def test_has_title(page: Page):
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")


def test_has_login_button(page: Page):
    page.goto("https://www.saucedemo.com/")
    expect(page.locator(".submit-button")).to_be_visible()

