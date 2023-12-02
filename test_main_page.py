from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    page = LoginPage(browser=browser, url=url)
    page.open()
    page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    url = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser=browser, url=url)
    page.open()
    page.should_be_login_link()
