from selenium.webdriver.common.by import By
from behave import given, when, then, step
from selenium.webdriver.support import expected_conditions as EC

SUBHEADER_LINK = (By.CSS_SELECTOR, '#zg_header a')
EACH_LINK = (By.CSS_SELECTOR, "a[href*='ref=zg_bsnr_tab']")


@given('Open Amazon BestSellers page')
def open_amazon_bestseller(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify there are {expected_count} subheader links')
def verify_subheader_links_count(context, expected_count):
    subheader_links = context.driver.find_elements(*SUBHEADER_LINK)  # [Webelement1, Webelement2, ..]
    assert len(subheader_links) == int(expected_count), f'Expected {expected_count} links, but got {len(expected_count)}'


@then('Clicks on each top link and verify that correct page opens')
def click_link(context):
    all_links = context.driver.find_elements(*EACH_LINK)
    for links in all_links:
        links.find_elements(*EACH_LINK).click()
        context.driver.wait.until(EC.url_contains('ref=zg_bs_tab'), 'Page did not open')




