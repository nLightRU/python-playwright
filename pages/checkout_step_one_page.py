from playwright.sync_api import Page

class CheckOutStepOne:
    TEST_ID_CLOSE_ERROR = 'error-button'
    TEST_ID_NAME = 'firstName'
    TEST_ID_LAST_NAME = 'lastName'
    TEST_ID_ZIP = 'postalCode'
    TEST_ID_CHECKOUT_STEP_TWO = 'continue'

    def __init__(self, page: Page):
        self.page = page
        self.name = page.get_by_test_id(self.TEST_ID_NAME)
        self.last_name = page.get_by_test_id(self.TEST_ID_LAST_NAME)
        self.zipcode = page.get_by_test_id(self.TEST_ID_ZIP)
        self.checkout_step_two = page.get_by_test_id(self.TEST_ID_CHECKOUT_STEP_TWO)


    def fill_name(self, name: str):
        self.name.fill(name)
    

    def fill_last_name(self, last_name: str):
        self.last_name.fill(last_name)


    def fill_zip(self, zipcode: str):
        self.zipcode.fill(zipcode)

    
    def go_to_checkout_step_two(self):
        self.checkout_step_two.click()