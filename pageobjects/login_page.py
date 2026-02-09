from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page=page
        self.username_input = page.get_by_test_id('username')
        self.pass_input = page.get_by_test_id('password')
        self.login_button = page.get_by_test_id('login-button')
    
    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.pass_input.fill(password)
        self.login_button.click()
        