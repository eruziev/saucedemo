from sys import platform

import pytest
from selenium import webdriver

from src.steps.login_steps import *

# Loading properties and start logging
# prop = utils.load_yaml(f"{utils.ROOT_DIR}/data/config.yaml")

utils.LOG = utils.create_logger(f"{utils.ROOT_DIR}/logs/{utils.get_str_day()}.log")

# variables
# HOST = prop['host']
# USER = prop['user']
# PASSWORD = prop['password']
chromedriver_path = "C:\Program Files\Python38\chromedriver.exe"

@pytest.fixture(scope="session", params=['Chrome'], autouse=True)
def driver(request):

    utils.LOG.info("************* SETUP *********************")
    utils.LOG.info("Initializing the browser ...")
    if platform == 'win32':
        if request.param == 'Chrome':
            # driver = webdriver.Chrome(chromedriver_path)
            driver = webdriver.Chrome()
            driver.implicitly_wait(20)
            driver.maximize_window()

    utils.LOG.info("The browser Initialized")
    # login_to_web(HOST, USER, PASSWORD)

    yield driver
    utils.LOG.info("***************** TEARDOWN *****************")
    utils.LOG.info("Closing the browser ...")
    driver.quit()
