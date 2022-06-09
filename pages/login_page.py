from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD)
        confirm_password_input = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)

        email_input.send_keys(email)
        password_input.send_keys(password)
        confirm_password_input.send_keys(password)

        confirm_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        confirm_button.click()
