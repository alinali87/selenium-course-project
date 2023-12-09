from .base_page import BasePage
from .locators import ProductPageLocators as Locators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*Locators.ADD_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()

    def read_title(self):
        return self.browser.find_element(*Locators.ITEM_TITLE).text

    def read_price(self):
        return self.browser.find_element(*Locators.ITEM_PRICE).text

    def should_be_item_added_message(self, title):
        assert self.is_element_present(*Locators.MESSAGE_ITEM_TITLE)
        item_title_text = self.browser.find_element(*Locators.MESSAGE_ITEM_TITLE).text
        assert item_title_text == title, \
            f'Expected {title}, got {item_title_text}'

    def should_be_cost_message(self, price):
        assert self.is_element_present(*Locators.MESSAGE_ITEM_PRICE)
        price_text = self.browser.find_element(*Locators.MESSAGE_ITEM_PRICE).text
        assert price_text == price, f'Expected {price}, got {price_text}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*Locators.MESSAGE_SUCCESS), 'Success message is presented, but should not be'

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*Locators.MESSAGE_SUCCESS), 'Success message is presented, but should disappear'
