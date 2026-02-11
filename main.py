import time
from typing import List
from playwright.sync_api import sync_playwright, Page, Locator

url = 'https://www.saucedemo.com/inventory.html'


def login(page: Page):
    page.locator('#user-name').fill('standard_user')
    page.locator('#password').fill('secret_sauce')
    page.get_by_role('button').click()


def get_inventory_list(page: Page) -> List[Locator]:
    items = page.get_by_test_id('inventory-item').all()
    return items


def cart_badge_count(page: Page) -> int:
    badge = page.get_by_test_id('shopping-cart-badge')
    return int(badge.text_content())
    
def item_price(price_str: str):
    return float(price_str[1:])

if __name__ == '__main__':
    with sync_playwright() as p:
        p.selectors.set_test_id_attribute('data-test')
        browser = p.chromium.launch(channel='chrome', headless=False)
        page = browser.new_page()
        page.goto('https://www.saucedemo.com')
        login(page)
        items = get_inventory_list(page)

        # Взаимодействуем с сайтом после логина

        price = items[0].get_by_test_id('inventory-item-price').text_content()
        print(price)
        print(item_price(price))

        time.sleep(5)