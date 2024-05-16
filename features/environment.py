import logging
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    # Setup logging
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_filename = f"report_{timestamp}.txt"
    log_filepath = os.path.join(os.path.dirname(__file__), '..', log_filename)

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filepath),
            logging.StreamHandler()
        ]
    )
    context.logger = logging.getLogger()

    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    context.driver = webdriver.Chrome(options=chrome_options)
    
def after_scenario(context, scenario):
    # Clear browser data
    context.driver.delete_all_cookies()
    context.driver.execute_script("window.localStorage.clear();")
    context.driver.execute_script("window.sessionStorage.clear();")
    context.logger.info("Cleared browser data after scenario")

def after_all(context):
    context.driver.quit()
    logging.shutdown()