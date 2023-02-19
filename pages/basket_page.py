from .base_page import BasePage
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def should_not_be_product_in_basket_opened_from_main_page(self):
        self.go_to_basket()
        assert self.is_not_element_present(By.CSS_SELECTOR, '#basket_formset'), 'Products shouldnt be in the basket'
        empty_basket_text = self.browser.find_element(By.CSS_SELECTOR, '#content_inner p').text
        assert empty_basket_text == "Your basket is empty. Continue shopping", \
            f'Should be "{empty_basket_text}" equal to "Your basket is empty. Continue shopping"'

    def should_not_be_product_in_basket_opened_from_product_page(self):
        self.go_to_basket()
        assert self.is_not_element_present(By.CSS_SELECTOR, '#basket_formset'), 'Products shouldnt be in the basket'
        empty_basket_text = self.browser.find_element(By.CSS_SELECTOR, '#content_inner p').text
        assert empty_basket_text == "Your basket is empty. Continue shopping", \
            f'Should be "{empty_basket_text}" equal to "Your basket is empty. Continue shopping"'
