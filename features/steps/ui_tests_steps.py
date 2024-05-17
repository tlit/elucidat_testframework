import logging
import re
import time

from behave import given, when, then
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.page_elements import pages

# Assert page presence
@then('I see the "{page_name}" page')
def wait_for_page_load(context, page_name):
    page = pages.get(page_name)
    if not page:
        context.logger.error(f"No page definition found for {page_name}\n")
        raise ValueError(f"No page definition found for {page_name}")
    for element in page.get_elements():
        try:
            WebDriverWait(context.driver, 20).until(
                EC.presence_of_element_located(element)
            )
            time.sleep(1)
        except TimeoutException:
            context.logger.error(f"Expected page '{page_name}' was not loaded. Missing element: {element}\n")
            raise AssertionError(f"Expected page '{page_name}' was not loaded. Missing element: {element}")

# Navigate to homepage URL
@given('I am on the course homepage')
def step_given_course_homepage(context):
    context.logger.info("Navigating to course homepage\n")
    context.driver.get("https://learning.elucidat.com/course/5c9126fd760e5-611a53751213a")
    time.sleep(1)
    wait_for_page_load(context, "homepage")

# Click Start on the homepage
@when('I click the START button')
def step_when_click_start_button(context):
    context.logger.info("Clicking the START button\n")
    start_button = context.driver.find_element(By.ID, "pa_5c9126fe3b767_p15577f075e9-textButton")
    start_button.click()
    wait_for_page_load(context, "start_page")

# Click the CardImage corresponding to Case 1 or 2
@when('I click CardImage {card_number}')
def step_when_click_cardimage1(context, card_number):
    context.logger.info(f"Clicking CardImage {card_number}\n")
    card_image = context.driver.find_element(By.ID, f"pa_5c9126fe3f4fb_p179d7b273e1-link--imgCard-{card_number}")
    card_image.click()
    wait_for_page_load(context, f"case_landing_page")

# Click the JUDGE THIS button on a Case Landing page
@when('I click the JUDGE THIS button')
def step_when_click_judge_this_button(context):
    context.logger.info("Clicking the JUDGE THIS button\n")
    judge_button = context.driver.find_element(By.XPATH, "//a[contains(@class, 'button--nav') and .//span[text()='JUDGE THIS']]")
    judge_button.click()
    wait_for_page_load(context, "case_judgement_page")

# Assert presence of the CardImage corresponding to Case 1 or 2
@then('I see CardImage {card_number}')
def step_then_see_card_image(context, card_number):
    context.logger.info(f"Checking for CardImage {card_number}\n")
    card_image_id = f"pa_5c9126fe3f4fb_p179d7b273e1-link--imgCard-{card_number}"
    try:
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, card_image_id))
        )
        card_image = context.driver.find_element(By.ID, card_image_id)
        if card_image.is_displayed():
            context.logger.info(f"CardImage {card_number} is displayed\n")
            assert True
        else:
            context.logger.error(f"CardImage {card_number} is not displayed\n")
            assert False, f"CardImage {card_number} is not displayed"
    except TimeoutException:
        context.logger.error(f"CardImage {card_number} was not found within the timeout period\n")
        assert False, f"CardImage {card_number} was not found within the timeout period"

# Assert the score on the homepage is an integer
@then('the current score displays an integer')
def step_then_current_score_displays_integer(context):
    context.logger.info("Checking if the current score displays an integer\n")
    score_div = context.driver.find_element(By.ID, "pa_5c9126fe3f4fb_p1552ed09ccb-text")
    score_text = score_div.text
    try:
        # Split the text at the colon and take the part after it
        score = int(score_text.split(':')[1].strip())
        if isinstance(score, int):
            assert True
        else:
            context.logger.error(f"The score is not an integer - Actual: {score}\n")
            assert False, "The score is not an integer"
    except (IndexError, ValueError) as e:
        context.logger.error(f"No valid score found in the text: {e}\n")
        raise AssertionError(f"No valid score found in the text: {e}")

# Assert the Vote button in a case is locked while no radiobutton is selected
@then('the Vote button is locked')
def step_then_vote_button_locked(context):
    context.logger.info("Checking if the Vote button is locked\n")
    button_xpath = "//a[@id='pa_5c9126fe47260_p15515116385-save_button']"
    try:
        WebDriverWait(context.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, button_xpath))
        )
        vote_button = context.driver.find_element(By.XPATH, button_xpath)
        is_locked = "fake_save_button--disabled" in vote_button.get_attribute("class")
        assert is_locked, "Vote button is not locked"
        context.logger.info("Vote button is locked\n")
    except TimeoutException:
        context.logger.error("Vote button is not present on the page\n")
        assert False, "Vote button is not present on the page"