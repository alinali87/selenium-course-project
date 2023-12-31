import time
import pytest
from random import choice
from string import ascii_uppercase, ascii_lowercase
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


url = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207'


@pytest.mark.user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = ProductPage(browser=browser, url=url)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser=browser, url=browser.current_url)
        email = str(time.time()) + "@fakemail.org"
        password = ''.join([choice(ascii_uppercase + ascii_lowercase + '1234567890') for _ in range(10)])
        login_page.register_new_user(email, password)
        login_page.should_be_authorized()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser=browser, url=url)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        url = f'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer1'
        page = ProductPage(browser=browser, url=url)
        page.open()
        title = page.read_title()
        price = page.read_price()
        page.add_to_basket()
        page.should_be_item_added_message(title)
        page.should_be_cost_message(price)


@pytest.mark.need_review
@pytest.mark.parametrize('tag',
                         [f'offer{n}' for n in range(7)] +
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


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser=browser, url=url)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason='Disappearing message is not implemented yet')
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser=browser, url=url)
    page.open()
    page.add_to_basket()
    page.should_be_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser=browser, url=url)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser=browser, url=url)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser=browser, url=browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser=browser, url=url)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser=browser, url=browser.current_url)
    basket_page.should_be_empty_basket()
