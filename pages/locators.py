from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, 'span>a')

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form button')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner')

