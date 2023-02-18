from pages.product_page import ProductPage


def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_added_to_cart()
