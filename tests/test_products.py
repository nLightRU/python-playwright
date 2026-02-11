import pytest
from playwright.sync_api import expect

from pages.products_page import ProductsPage

@pytest.fixture
def products_opened(auth_context, products_url):
    page = auth_context.new_page()
    page.goto(products_url)
    i = ProductsPage(page)
    return i


def test_open_items_page(products_opened):
    products_opened.check_title()
    assert products_opened.cart_count() == 0


def test_sort_by_price_asc(products_opened: ProductsPage):
    products_prices_asc = [
        products_opened.item_price(i) for i in range(len(products_opened.items))
    ]
    products_prices_asc.sort()

    products_opened.sort_by_price_asc()

    products_prices = [
        products_opened.item_price(i) for i in range(len(products_opened.items))
    ]

    assert products_prices == products_prices_asc


def test_sort_by_price_desc(products_opened: ProductsPage):
    products_prices_desc = [
        products_opened.item_price(i) for i in range(len(products_opened.items))
    ]
    products_prices_desc.sort(reverse=True)

    products_opened.sort_by_price_desc()

    products_prices = [
        products_opened.item_price(i) for i in range(len(products_opened.items))
    ]

    assert products_prices == products_prices_desc


def test_add_to_cart(products_opened: ProductsPage):
    products_opened.add_to_cart(0)
    assert products_opened.cart_count() == 1


def test_remove_from_cart(products_opened: ProductsPage):
    products_opened.add_to_cart(0)
    products_opened.remove_from_cart(0)
    assert products_opened.cart_count() == 0