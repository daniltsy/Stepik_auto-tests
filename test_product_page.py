from pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('params', ["?promo=offer0",
                                  "?promo=offer1",
                                  "?promo=offer2",
                                  "?promo=offer3",
                                  "?promo=offer4",
                                  "?promo=offer5",
                                  "?promo=offer6",
                                  pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                  "?promo=offer8",
                                  "?promo=offer9"])
def test_guest_can_add_product_to_cart(browser, params):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{params}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_added_to_cart()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message_after_adding_product_to_basket()


def test_guest_cant_see_success_message_before_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message_before_adding_product_to_basket()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_message_disappeared_after_adding_product_to_basket()
