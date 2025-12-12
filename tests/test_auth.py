import pytest
from playwright.sync_api import Playwright, Page, expect

# To Do: Check placeholder
# To Do: Вынести сообщения об ошибках отдельно

# Тест успешной авторизации в сервисе
@pytest.mark.auth
def test_success_auth(playwright: Playwright, page: Page):
    playwright.selectors.set_test_id_attribute('data-test')
    page.goto('https://www.saucedemo.com/')
    page.get_by_test_id('username').fill('standard_user')
    page.get_by_test_id('password').fill('secret_sauce')
    page.get_by_test_id('login-button').click()
    expect(page.get_by_test_id('title')).to_be_visible()
    expect(page.get_by_test_id('title')).to_have_text('Products')


# Тест выхода из аккаунта
# Здесь надо тестить сразу на залогиненом аккаунте!!!!
@pytest.mark.auth
@pytest.mark.skip(reason="Not implemented yet")
def test_logout(playwright: Playwright, page: Page):
    playwright.selectors.set_test_id_attribute('data-test')
    page.goto('https://www.saucedemo.com/')


@pytest.mark.auth
def test_locked_out_user(playwright: Playwright, page: Page):
    playwright.selectors.set_test_id_attribute('data-test')
    page.goto('https://www.saucedemo.com/')
    page.get_by_test_id('username').fill('locked_out_user')
    page.get_by_test_id('password').fill('secret_sauce')
    page.get_by_test_id('login-button').click()
    expect(page.get_by_test_id('error')).to_be_visible()
    expect(page.get_by_text('Epic sadface: Sorry, this user has been locked out.')).to_be_visible()


# Появляется ошибка если поля пустые
@pytest.mark.auth
@pytest.mark.negative
def test_empty_fields(playwright: Playwright, page: Page):
    playwright.selectors.set_test_id_attribute('data-test')
    page.goto('https://www.saucedemo.com/')
    page.locator('id=login-button').click()
    expect(page.get_by_test_id('error')).to_be_visible()
    expect(page.get_by_text('Epic sadface: Username is required')).to_be_visible()


# Появляется ошибка если пароль неправильный
@pytest.mark.auth
@pytest.mark.negative
def test_wrong_password(playwright: Playwright, page: Page):
    playwright.selectors.set_test_id_attribute('data-test')
    page.goto('https://www.saucedemo.com/')
    page.get_by_test_id('username').fill('standard_user')
    page.get_by_test_id('password').fill('1234666')
    page.get_by_test_id('login-button').click()
    expect(page.get_by_test_id('error')).to_be_visible()
    expect(page.get_by_text('Epic sadface: Username and password do not match any user in this service')).to_be_visible()


# Появляется ошибка если имя пользователя неправильное, а пароль правильный
@pytest.mark.auth
def test_wrong_username(playwright: Playwright, page: Page):
    playwright.selectors.set_test_id_attribute('data-test')
    page.goto('https://www.saucedemo.com/')
    page.get_by_test_id('username').fill('qweasd')
    page.get_by_test_id('password').fill('secret_sauce')
    page.get_by_test_id('login-button').click()
    expect(page.get_by_test_id('error')).to_be_visible()
    expect(page.get_by_text('Epic sadface: Username and password do not match any user in this service')).to_be_visible()


# Наличие плейсхолдеров и их правильное значение
@pytest.mark.UI
def test_placeholders(playwright: Playwright, page: Page):
    playwright.selectors.set_test_id_attribute('data-test')
    page.goto('https://www.saucedemo.com/')
    expect(page.get_by_test_id('username')).to_have_attribute('placeholder', 'Username')
    expect(page.get_by_test_id('password')).to_have_attribute('placeholder', 'Password')


# После неправильной авторизации крестиком можно закрыть ошибку
# Пока не знаю как проверять CSS свойства элементов
@pytest.mark.UI
def test_error_close(playwright: Playwright, page: Page):
    playwright.selectors.set_test_id_attribute('data-test')
    page.goto('https://www.saucedemo.com/')
    page.get_by_test_id("login-button").click()
    expect(page.get_by_test_id('error')).to_be_visible()
    page.get_by_test_id('error-button').click()
    expect(page.get_by_test_id('error')).not_to_be_visible()