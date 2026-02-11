import pytest, time
from playwright.sync_api import Page

from pages.cart_page import CartPage

@pytest.fixture
def cart_opened(auth_context, cart_url):
    page = auth_context.new_page()
    page.goto(cart_url)
    page.evaluate("localStorage.setItem('cart-contents', '[1, 2, 3]');")
    page.reload()

    c = CartPage(page)

    return c


def test_cart_open(cart_opened: CartPage):
    cart_opened.check_title()


def test_remove_from_cart(cart_opened: CartPage):
    old_count = cart_opened.items_count()
    cart_opened.remove_first_item()
    assert cart_opened.items_count() == (old_count - 1)
    