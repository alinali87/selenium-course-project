from .base_page import BasePage
from .locators import LoginPageLocators as Locators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, f'Expected "login" in url, got {self.browser.current_url} instead'

    def should_be_login_form(self):
        assert self.is_element_present(*Locators.LOGIN_FORM), 'Login form is not present'

    def should_be_register_form(self):
        assert self.is_element_present(*Locators.REGISTER_FORM), 'Register form is not present'
