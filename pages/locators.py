from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BUTTON_VIEW_CART = (By.LINK_TEXT, 'View basket')
    BUTTON_CART = (By.CSS_SELECTOR, '.btn-cart')


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    ITEM_TITLE = (By.CSS_SELECTOR, 'div.product_main h1')
    ITEM_PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    MESSAGE_SUCCESS = (By.CSS_SELECTOR, '#messages .alert-success:nth-child(1)')
    MESSAGE_ITEM_TITLE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) strong')
    MESSAGE_ITEM_PRICE = (By.CSS_SELECTOR, '#messages > div:nth-child(3) strong')


class BasketPageLocators:
    TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
