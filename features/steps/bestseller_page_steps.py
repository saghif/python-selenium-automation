from selenium.webdriver.common.by import By
from behave import given, when, then, step


SUBHEADER_LINK = (By.CSS_SELECTOR, '#zg_header a')


@given('Open Amazon BestSellers page')
def open_amazon_bestseller(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify there are {expected_count} subheader links')
def verify_subheader_links_count(context, expected_count):
    subheader_links = context.driver.find_elements(*SUBHEADER_LINK)  # [Webelement1, Webelement2, ..]
    assert len(subheader_links) == int(expected_count), f'Expected {expected_count} links, but got {len(expected_count)}'