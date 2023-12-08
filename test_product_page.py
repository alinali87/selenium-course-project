import pytest
from pages.product_page import ProductPage


@pytest.mark.parametrize('tag', [f'offer{n}' for n in range(7)] +
                                [pytest.param('offer7', marks=pytest.mark.xfail)] +
                                 [f'offer{n}' for n in range(8, 10)])
def test_guest_can_add_product_to_basket(browser, tag):
    url = f'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo={tag}'
    page = ProductPage(browser=browser, url=url)
    page.open()
    title = page.read_title()
    price = page.read_price()
    page.add_to_basket()
    page.should_be_item_added_message(title)
    page.should_be_cost_message(price)
