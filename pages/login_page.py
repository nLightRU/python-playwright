from playwright.sync_api import Page, expect

class LoginPage:
    
    TEST_ID_USERNAME_INPUT = 'username'
    TEST_ID_PASSWORD_INPUT = 'password'
    TEST_ID_LOGIN_BUTTON = 'login-button'

    def __init__(self, page: Page):
        self.page=page
        self.username_input = page.get_by_test_id(self.TEST_ID_USERNAME_INPUT)
        self.pass_input = page.get_by_test_id(self.TEST_ID_PASSWORD_INPUT)
        self.login_button = page.get_by_test_id(self.TEST_ID_LOGIN_BUTTON)

    
    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.pass_input.fill(password)
        self.login_button.click()
    
    def get_login_error(self, error_message=''):
        ...
        