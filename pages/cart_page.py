from playwright.sync_api import Page

class CartPage:
    TEST_ID_CONTINUE_SHOPPING = 'continue-shopping'
    TEST_ID_TO_CHECKOUT = 'checkout'

    def __init__(self, page: Page):
        self.page = page
