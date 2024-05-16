import logging
import re
import time

from behave import given, when, then
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from page_elements import pages

logger = logging.getLogger('behave')

@then('I see the "{page_name}" page')
def wait_for_page_load(context, page_name):
    page = pages.get(page_name)
    if not page:
        raise ValueError(f"No page definition found for {page_name}")
    
    for element in page.get_elements():
        try:
            WebDriverWait(context.driver, 20).until(
                EC.presence_of_element_located(element)
            )
        except TimeoutException:
            raise TimeoutException(f"Expected page '{page_name}' was not loaded.")

@given('I am on the course homepage')
def step_given_course_homepage(context):
    logger.info("Navigating to course homepage")
    context.driver.get("https://learning.elucidat.com/course/5c9126fd760e5-611a53751213a")
    time.sleep(5)
    wait_for_page_load(context, "homepage")

@when('I click the START button')
def step_when_click_start_button(context):
    logger.info("Clicking the START button")
    start_button = context.driver.find_element(By.ID, "pa_5c9126fe3b767_p15577f075e9-textButton")
    start_button.click()
    wait_for_page_load(context, "start_page")
    
@when('I click CardImage {card_number}')
def step_when_click_cardimage1(context, card_number):
    logger.info(f"Clicking CardImage {card_number}")
    card_image = context.driver.find_element(By.ID, f"pa_5c9126fe3f4fb_p179d7b273e1-link--imgCard-{card_number}")
    card_image.click()
    wait_for_page_load(context, f"case_landing_page")
    
@when('I click the JUDGE THIS button')
def step_when_click_judge_this_button(context):
    logger.info("Clicking the JUDGE THIS button")
    judge_button = context.driver.find_element(By.XPATH, "//a[contains(@class, 'button--nav') and .//span[text()='JUDGE THIS']]")
    judge_button.click()
    wait_for_page_load(context, "case_judgement_page")

@then('I see CardImage {card_number}')
def step_then_see_card_image(context, card_number):
    logger.info(f"Checking for CardImage {card_number}")
    card_image_id = f"pa_5c9126fe3f4fb_p179d7b273e1-link--imgCard-{card_number}"
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, card_image_id))
    )
    card_image = context.driver.find_element(By.ID, card_image_id)
    assert card_image.is_displayed(), f"CardImage {card_number} is not displayed"


@then('the current score displays an integer')
def step_then_current_score_displays_integer(context):
    logger.info("Checking if the current score displays an integer")
    # Locate the paragraph element by its style attribute
    score_paragraph = context.driver.find_element(By.CSS_SELECTOR, 'p[style="text-align:center;"]')
    
    # Extract the text content of the paragraph
    score_text = score_paragraph.text
    
    # Use regular expression to find the integer score after the colon
    match = re.search(r'Your score so far:(\d+)', score_text)
    
    # Check if a match is found and extract the integer score
    if match:
        score = int(match.group(1))
        assert isinstance(score, int), "The score is not an integer"
    else:
        raise AssertionError("No integer score found in the text")
