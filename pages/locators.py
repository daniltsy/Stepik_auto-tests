from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, 'span>a')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class BasketPageLocators:
    BASKET_FORMSET = (By.CSS_SELECTOR, '#basket_formset')
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '[name = "registration_submit"]')
    REGISTRATION_SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.wicon')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form button')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner')
    PRODUCT_NAME_BEFORE_ADD_TO_BASKET = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_COST_BEFORE_ADD_TO_BASKET = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_NAME_AFTER_ADD_TO_BASKET = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRODUCT_COST_AFTER_ADD_TO_BASKET = (By.CSS_SELECTOR, '.alert-info strong')

