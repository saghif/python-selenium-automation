from selenium.webdriver.common.by import By
from behave import given, when, then, step
from selenium.webdriver.support import expected_conditions as EC

SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
HAM_MENU_BTN = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, 'td.navFooterDescItem a')
CLICK_PRODUCT = (By.CSS_SELECTOR, 'span.a-price-whole')
ADD_CART_BTN = (By.CSS_SELECTOR, '#add-to-cart-button')
CARD_COUNT = (By.CSS_SELECTOR, '#nav-cart-count')
SIGN_IN_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for {search_word}')
def search_amazon(context, search_word):
    context.driver.find_element(*SEARCH_INPUT).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()


@when('Click on Add to cart btn')
def click_add(context):
    context.driver.find_element(*ADD_CART_BTN).click()


@when('Click on button from SignIn popup')
def click_sign_in_btn(context):
    sign_in_btn = context.driver.wait.until(
        EC.element_to_be_clickable(SIGN_IN_BTN), 'Sign in btn not clickable'
    )
    sign_in_btn.click()


@then('Verify hamburger menu btn present')
def verify_ham_menu(context):
    context.driver.find_element(*HAM_MENU_BTN)


@then('Verify there are {expected_amount} footer links')
def verify_footer_links_count(context, expected_amount):
    expected_amount = int(expected_amount)  # '38' => 38
    footer_links = context.driver.find_elements(*FOOTER_LINKS)  # [Webelement1, Webelement2, ..]
    assert len(footer_links) == expected_amount, f'Expected {expected_amount} links, but got {len(footer_links)}'


@then('Verify cart has {expected_number} item')
def verify_cart_count(context, expected_number):
    expected_number = int(expected_number)
    card_count = context.driver.find_elements(*CARD_COUNT)
    assert len(card_count) == expected_number, f'Expected {expected_number} links, but got {len(card_count)}'
