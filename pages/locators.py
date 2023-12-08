from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    ITEM_TITLE = (By.CSS_SELECTOR, 'div.product_main h1')
    ITEM_PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    MESSAGE_ITEM_TITLE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) strong')
    MESSAGE_ITEM_PRICE = (By.CSS_SELECTOR, '#messages > div:nth-child(3) strong')
