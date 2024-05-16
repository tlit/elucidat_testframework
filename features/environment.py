from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_scenario(context, scenario):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    context.driver = webdriver.Chrome(options=chrome_options)
    
def after_scenario(context, scenario):
    context.driver.quit()
