from playwright.sync_api import Page, expect

class CartPage:
    TEST_ID_TITLE = 'title'
    TEST_ID_CONTINUE_SHOPPING = 'continue-shopping'
    TEST_ID_TO_CHECKOUT = 'checkout'
    TEST_ID_TO_SHOPPING = 'continue-shopping'
    TEST_ID_CART_ITEM = 'inventory-item'

    TITLE_TEXT = 'Your Cart'
    
    def __init__(self, page: Page):
        self.page = page
        self.items = page.get_by_test_id(self.TEST_ID_CART_ITEM).all()
        self.to_checkout = page.get_by_test_id(self.TEST_ID_TO_CHECKOUT)
        self.to_shopping = page.get_by_test_id(self.TEST_ID_TO_SHOPPING)
    

    def check_title(self):
        title = self.page.get_by_test_id(self.TEST_ID_TITLE)
        expect(title).to_have_text(self.TITLE_TEXT)
    

    def remove_first_item(self):
        self.items[0].get_by_role('button').click()
        self.items = self.page.get_by_test_id(self.TEST_ID_CART_ITEM).all()


    def remove_item(self, item_index: int):
        self.items[item_index].get_by_role('button').click()
        self.items = self.page.get_by_test_id(self.TEST_ID_CART_ITEM).all()


    def items_count(self) -> int:
        return len(self.items)


    def go_to_checkout(self):
        self.to_checkout.click()

    
    def go_to_shopping(self):
        self.to_shopping.click()