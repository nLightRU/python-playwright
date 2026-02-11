from playwright.sync_api import Page, Locator, expect

class ProductsPage:
    TEST_ID_TITLE = 'title'
    TEST_ID_SORT_SELECT = 'product-sort-container'
    TEST_ID_CART_BADGE = 'shopping-cart-badge'


    PAGE_TITLE = 'Products'

    SORT_NAME_ASC = 'az'
    SORT_NAME_DESC = 'za'
    SORT_PRICE_ASC = 'lohi'
    SORT_PRICE_DESC = 'hilo'
    
    TEST_ID_INVENTORY_ITEM = 'inventory-item'
    TEST_ID_ITEM_NAME  = 'inventory-item-name'
    TEST_ID_ITEM_DESC = 'inventory-item-desc'
    TEST_ID_ITEM_PRICE = 'inventory-item-price'

    BUTTON_ADD_TEXT = 'Add to cart'
    BUTTON_REMOVE_TEXT = 'Remove'


    def __init__(self, page: Page):
        self.page = page
        self.items = page.get_by_test_id(self.TEST_ID_INVENTORY_ITEM).all()
        self.sort_select = page.get_by_test_id(self.TEST_ID_SORT_SELECT)


    def cart_count(self) -> int:
        """
        If any product in cart, badge wiil be appeared and func return badge count
        If no product in cart, badge won't be visible and func return 0
        """
        if self.page.get_by_test_id(self.TEST_ID_CART_BADGE).is_visible():
            return int(self.page.get_by_test_id(self.TEST_ID_CART_BADGE).text_content())
        else:
            return 0


    def check_title(self):
        expect(self.page.get_by_test_id(self.TEST_ID_TITLE)).to_have_text(self.PAGE_TITLE)   


    def sort_by_name_asc(self):
        self.sort_select.select_option(self.SORT_NAME_ASC)


    def sort_by_name_desc(self):
        self.sort_select.select_option(self.SORT_NAME_DESC)


    def sort_by_price_asc(self):
        self.sort_select.select_option(self.SORT_PRICE_ASC)


    def sort_by_price_desc(self):
        self.sort_select.select_option(self.SORT_PRICE_DESC)


    def add_to_cart(self, item_index: int):
        self.items[item_index].get_by_text(self.BUTTON_ADD_TEXT).click()
    

    def remove_from_cart(self, item_index: int):
        self.items[item_index].get_by_text(self.BUTTON_REMOVE_TEXT).click()


    def item_price(self, item_index: int) -> float:
        price_str = self.items[item_index].get_by_test_id(self.TEST_ID_ITEM_PRICE).inner_text()
        return float(price_str[1:])
