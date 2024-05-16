from selenium.webdriver.common.by import By

class Page:
    def __init__(self, name, *elements):
        self.name = name
        self.elements = elements

    def get_elements(self):
        return self.elements

# Page objects containing elements used to tell when that page is loaded

homepage = Page(
    "homepage",
    (By.XPATH, "//a[contains(@class, 'button--nav') and .//span[text()='START']]")
)

start_page = Page(
    "start_page",
    (By.ID, "pa_5c9126fe3f4fb_p179d7b273e1-link--imgCard-1"), # Case 1
    (By.ID, "pa_5c9126fe3f4fb_p179d7b273e1-link--imgCard-2")  # Case 2
)

case_landing_page = Page (
    "case_landing_page",
    (By.XPATH, "//a[contains(@id, '_p15564daa856-textButton')]") # Matches Judge This button for case 1 & 2
)

case1_landing_page = Page (
    "case1_landing_page",
    (By.ID, "pa_5c9126fe434ba_p15564daa856-textButton") # Judge This button
)

case2_landing_page = Page(
    "case2_landing_page",
    (By.ID, "pa_5c9126ff8a53e_p15564daa856-textButton")  # Judge This button
)

case_judgement_page = Page (
    "case_judgement_page",
    (By.XPATH, "//a[contains(@id, '_p15515116385-save_button')]") # Matches VOTE button for case 1 & 2
)

case1_judgement_page = Page (
    "case2_judgement_page",
    (By.ID, "pa_5c9126fe47260_p15515116385-save_button") # VOTE button
)

case2_judgement_page = Page (
    "case2_judgement_page",
    (By.ID, "pa_5c9126ff8e016_p15515116385-save_button") # VOTE button
)

# Dict of pages
pages = {
    "homepage": homepage,
    "start_page": start_page,
    "case_landing_page": case_landing_page,
    "case1_landing_page": case1_landing_page,
    "case2_landing_page": case2_landing_page,
    "case_judgement_page": case_judgement_page,
    "case1_judgement_page": case1_judgement_page,
    "case2_judgement_page": case2_judgement_page
}
