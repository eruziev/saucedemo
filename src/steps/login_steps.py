from src.pages.login_page import *
import src.utilities as utils
import time


def login_to_web(driver, host, user, password):

    login_page = Login(driver)

    utils.LOG.info(f"Launching and logging in to {host}")
    driver.get(host)
    time.sleep(3)
    login_page.enter_username(user)
    login_page.enter_password(password)
    time.sleep(1)
    login_page.click_login()
    utils.LOG.info("Logged in to the platform.")
