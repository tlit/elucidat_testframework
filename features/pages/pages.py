from selenium.webdriver.common.by import By

class Page:
    def __init__(self, name, *elements):
        self.name = name
        self.elements = elements

    def get_elements(self):
        return self.elements

# Define the elements for each page
homepage = Page(
    "homepage",
    (By.ID, "pa_5c9126fe3b767_p15577f075e9-textButton")
)

start_page = Page(
    "start_page",
    (By.ID, "pa_5c9126fe3f4fb_p179d7b273e1-link--imgCard-1"),
    (By.ID, "pa_5c9126fe3f4fb_p179d7b273e1-link--imgCard-2")
)

# Store the pages in a dictionary for easy access
pages = {
    "homepage": homepage,
    "start_page": start_page
}
