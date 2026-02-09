from pytest import fixture
from playwright.sync_api import Playwright, Page, expect

from pageobjects.login_page import LoginPage 


def test_login(playwright: Playwright, page: Page, url, items_url):
    playwright.selectors.set_test_id_attribute('data-test')
    page.goto(url)
    p = LoginPage(page)
    p.login(username='standard_user', password='secret_sauce')
    expect(p.page).to_have_url(items_url)


def test_no_input(playwright: Playwright, page: Page, no_input_error_message):
    playwright.selectors.set_test_id_attribute('data-test')
    page.goto('https://www.saucedemo.com/')
    p = LoginPage(page)
    p.login(username='', password='')
    expect(p.page.get_by_test_id('error')).to_have_text(no_input_error_message)