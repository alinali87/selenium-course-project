from .base_page import BasePage
from .locators import BasketPageLocators as Locators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*Locators.BASKET_ITEMS)
        assert self.is_element_present(*Locators.TEXT_EMPTY_BASKET)
        empty_text = self.browser.find_element(*Locators.TEXT_EMPTY_BASKET).text
        assert 'Your basket is empty' in empty_text, f'Expected "Your basket is empty", got {empty_text} instead'
