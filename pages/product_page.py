from .base_page import BasePage
from pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def should_be_product_added_to_cart(self):
        product_name = self.browser.find_element(By.CSS_SELECTOR, '.product_main h1').text
        product_cost = self.browser.find_element(By.CSS_SELECTOR, '.product_main .price_color').text
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()
        self.solve_quiz_and_get_code()
        product_name_confirm = self.browser.find_element(By.XPATH, '//*[@id="messages"]/div[1]/div/strong').text
        product_cost_confirm = self.browser.find_element(By.CSS_SELECTOR, '.alert-info strong').text
        assert product_name == product_name_confirm, 'Product name doesnt match'
        assert product_cost == product_cost_confirm, 'Product cost doesnt match'
