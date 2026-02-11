from playwright.sync_api import Page, expect

class LoginPage:
    
    TEST_ID_USERNAME_INPUT = 'username'
    TEST_ID_PASSWORD_INPUT = 'password'
    TEST_ID_LOGIN_BUTTON = 'login-button'
    TEST_ID_ERROR_TEXT = 'error'
    TEST_ID_CLOSE_ERROR = 'error-button'

    ERROR_WRONG_INPUT = 'Epic sadface: Username and password do not match any user in this service'
    ERROR_NO_USERNAME_INPUT = 'Epic sadface: Username is required'
    ERROR_NO_PASSWORD_INPUT = 'Epic sadface: Password is required'

    def __init__(self, page: Page):
        self.page=page
        self.username_input = page.get_by_test_id(self.TEST_ID_USERNAME_INPUT)
        self.pass_input = page.get_by_test_id(self.TEST_ID_PASSWORD_INPUT)
        self.login_button = page.get_by_test_id(self.TEST_ID_LOGIN_BUTTON)
        self.error = page.get_by_test_id(self.TEST_ID_ERROR_TEXT)
        self.close_error = page.get_by_test_id(self.TEST_ID_CLOSE_ERROR)


    def fill_username(self, username: str):
        self.username_input.fill(username)


    def fill_password(self, password: str):
        self.pass_input.fill(password)


    def click_login(self):
        self.login_button.click()


    def check_wrong_input_error(self):
        return expect(self.error).to_have_text(self.ERROR_WRONG_INPUT)
    
    
    def check_no_username_error(self):
        return expect(self.error).to_have_text(self.ERROR_NO_USERNAME_INPUT)
    

    def check_no_password_error(self):
        return expect(self.error).to_have_text(self.ERROR_NO_PASSWORD_INPUT)
        