from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_basket_button(browser):
    browser.get(url)
    buttons = browser.find_elements(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    assert len(buttons) == 1, 'No [Add to Busket] button'
