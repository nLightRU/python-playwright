from playwright.sync_api import Playwright, Page, expect

from pages.login_page import LoginPage 


def test_login(page: Page, shop_url, items_url):
    page.goto(shop_url)
    p = LoginPage(page)
    p.fill_username('standard_user')
    p.fill_password('secret_sauce')
    p.click_login()
    expect(p.page).to_have_url(items_url)


def test_no_input(page: Page, shop_url):
    page.goto(shop_url)
    p = LoginPage(page)
    p.fill_username('')
    p.fill_password('')
    p.click_login()
    p.check_no_username_error()


def test_wrong_password(page: Page, shop_url):
    page.goto(shop_url)
    p = LoginPage(page)
    p.fill_username('standard_user')
    p.fill_password('123123')
    p.click_login()
    p.check_wrong_input_error()
    
    
    
