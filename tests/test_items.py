import time

from playwright.sync_api import Playwright, BrowserContext, Locator, expect


# Меняется вид кнопки, счётчик у корзины
# Параметризация
def test_add_to_cart(playwright: Playwright, context: BrowserContext, items_url):
    playwright.selectors.set_test_id_attribute('data-test')
    context.add_cookies([{
        'name': 'session-username',
        'value': 'standard_user',
        'domain': 'www.saucedemo.com',
        'path': '/'
    }])
    page = context.new_page()
    page.goto(items_url)
    items = page.get_by_test_id('inventory-item').all()
    button = items[0].get_by_role('button')
    button.click()
    expect(items[0].get_by_test_id('remove-sauce-labs-backpack')).to_be_visible()


def test_add_to_cart_multiple(playwright: Playwright, context: BrowserContext, items_url):
    playwright.selectors.set_test_id_attribute('data-test')
    context.add_cookies([{
        'name': 'session-username',
        'value': 'standard_user',
        'domain': 'www.saucedemo.com',
        'path': '/'
    }])

    page = context.new_page()
    page.goto(items_url)

    items = page.get_by_test_id('inventory-item-description').all()
    for i in range(3):
        button : Locator = items[i].get_by_role('button').click()
    
    expect(page.get_by_test_id('shopping-cart-badge')).to_have_text('3')



# page.evaluate("localStorage.setItem('cart-contents', '[4]')") не работает, походу надо нажимать кнопку "Добавить"
def test_remove_from_cart(playwright: Playwright, context: BrowserContext, items_url):
    playwright.selectors.set_test_id_attribute('data-test')
    context.add_cookies([{
        'name': 'session-username',
        'value': 'standard_user',
        'domain': 'www.saucedemo.com',
        'path': '/'
    }])
    page = context.new_page()
    page.goto(items_url)
    items = page.get_by_test_id('inventory-item').all()

    # Добавляем первый товар в корзину
    button = items[0].get_by_role('button')
    button.click()
    expect(items[0].get_by_test_id('remove-sauce-labs-backpack')).to_be_visible()

    # Убираем первый товар из корзины
    button = items[0].get_by_role('button')
    button.click()
    expect(items[0].get_by_test_id('add-to-cart-sauce-labs-backpack')).to_be_visible()


def test_go_to_cart():
    ...


def test_open_item_page():
    ...