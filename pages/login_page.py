from .base_page import BasePage
from pages.locators import LoginPageLocators
from pages.locators import BasePageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' does not a part of url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login Form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration Form is not presented"

    def register_new_user(self, email, password):
        send_email = self.element_to_action(By.CSS_SELECTOR, '#id_registration-email')
        send_email.send_keys(f"{email}")
        send_password = self.element_to_action(By.CSS_SELECTOR, '#id_registration-password1')
        send_password.send_keys(f"{password}")
        send_password_confirm = self.element_to_action(By.CSS_SELECTOR, '#id_registration-password2')
        send_password_confirm.send_keys(f"{password}")
        registration_button = self.element_to_action(By.CSS_SELECTOR, '[name = "registration_submit"]')
        registration_button.click()
        assert self.is_element_present(By.CSS_SELECTOR, '.wicon'), 'Something wrong with the registration'


