from playwright.sync_api import Page, Locator

class ItemsPage:

    TEST_ID_SORT_SELECT = 'product-sort-container'
    TEST_ID_INVENTORY_ITEM = 'inventory-item'
    TEST_ID_ITEM_ADD_TO_CART_BUTTON = ''
    TEST_ID_ITEM_NAME  = 'inventory-item-name'
    TEST_ID_ITEM_DESC = 'inventory-item-desc'
    TEST_ID_ITEM_PRICE = 'inventory-item-price'


    def __init__(self, page: Page):
        self.page = page
        self.items = page.get_by_test_id(self.TEST_ID_INVENTORY_ITEM).all()


    def get_item(self, index: int) -> Locator:
        """
        Возвращает IndexError если некорректный индекс
        """
        if index >= len(self.items):
            raise IndexError
        
        return self.items[index]


    def add_item_to_cart(self, index: int):
        """
        Добавляет элемент в корзину
        Возвращает IndexError если некорректный индекс
        """
        try:
            item = self.get_item(index)
        except:
            raise Exception
        
        item.get_by_role('button').click()


    def open_product_page(self, index: int):
        try:
            item = self.get_item(index)
        except:
            raise Exception

        item.get_by_test_id(self.TEST_ID_ITEM_NAME).click()


    def sort_by_name_asc(self):
        self.page.get_by_test_id(self.TEST_ID_SORT_SELECT)


    def sort_by_name_desc(self):
        ...


    def sort_by_price_asc(self):
        ...


    def sort_by_price_desc(self):
        ...