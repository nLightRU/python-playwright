from playwright.sync_api import Playwright, Page, expect, Browser

from pageobjects.login_page import LoginPage 


def test_login(playwright: Playwright, page: Page):
    playwright.selectors.set_test_id_attribute('data-test')
    page.goto('https://www.saucedemo.com/')
    p = LoginPage(page)
    p.login(username='standard_user', password='secret_sauce')
    expect(p.page).to_have_url('https://www.saucedemo.com/inventory.html')


def test_no_input(playwright: Playwright, page: Page):
    playwright.selectors.set_test_id_attribute('data-test')
    page.goto('https://www.saucedemo.com/')
    p = LoginPage(page)
    p.login(username='', password='')
    expect(p.page.get_by_test_id('error')).to_have_text('Epic sadface: Username is required')