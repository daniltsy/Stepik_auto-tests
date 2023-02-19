from .base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket_opened_from_main_page(self):
        self.go_to_basket()
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET), 'Products shouldnt be in the basket'
        empty_basket_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        assert empty_basket_text == "Your basket is empty. Continue shopping", \
            f'Should be "{empty_basket_text}" equal to "Your basket is empty. Continue shopping"'

    def should_not_be_product_in_basket_opened_from_product_page(self):
        self.go_to_basket()
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET), 'Products shouldnt be in the basket'
        empty_basket_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        assert empty_basket_text == "Your basket is empty. Continue shopping", \
            f'Should be "{empty_basket_text}" equal to "Your basket is empty. Continue shopping"'
