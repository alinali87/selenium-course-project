import pytest
from selenium import webdriver


# TODO: Добавьте туда файл conftest.py из предыдущего модуля. Убедитесь дополнительно, что там есть параметр для задания языка интерфейса, по умолчанию равный "en".
@pytest.fixture(scope='function')
def browser():
    print('\nstart browser for a test...')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser...')
    browser.quit()
