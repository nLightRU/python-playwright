from playwright.sync_api import Playwright, Page, expect

from pages.login_page import LoginPage 


def test_login(page: Page, base_url, items_url):
    page.goto(base_url)
    p = LoginPage(page)
    p.login(username='standard_user', password='secret_sauce')
    expect(p.page).to_have_url(items_url)


def test_no_input(page: Page, base_url, no_input_error_message):
    page.goto(base_url)
    p = LoginPage(page)
    p.login(username='', password='')
    expect(p.page.get_by_test_id('error')).to_have_text(no_input_error_message)


def test_wrong_password(page: Page, base_url):
    p = LoginPage(page.goto(base_url))
    p.login(username='standard_user', password='123')
    
