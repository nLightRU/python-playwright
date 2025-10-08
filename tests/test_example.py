import pytest
from playwright.sync_api import Page, expect

def test_health(page: Page):
    assert 1

@pytest.mark.smoke
def test_has_title(page: Page):
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")

@pytest.mark.skip(reason="Wrong test")
def test_has_login_button(page: Page):
    page.goto("https://www.saucedemo.com/")
    expect(page.get_by_role("submit")).to_be_visible()

