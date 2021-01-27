import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium import webdriver

import src.utilities as utils


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_element_by_xpath(self, xpath):
        try:
            # element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            element.click()
        except (NoSuchElementException, TimeoutException):
            self.take_screenshot('ErrorClickElement')
            utils.LOG.error(f"element was not found by {xpath}")
            pytest.fail(f"Unable to click element by {xpath}")

    def click_element_by_id(self, elem_id):
        try:
            element = self.wait.until(EC.presence_of_element_located((By.ID, elem_id)))
            element.click()
        except (NoSuchElementException, TimeoutException):
            self.take_screenshot('ErrorClickElement')
            utils.LOG.error(f"element was not found by {elem_id}")
            pytest.fail(f"Unable to click element by {elem_id}")

    def enter_text_by_xpath(self, xpath, phrase):
        try:
            element = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            element.clear()
            element.send_keys(phrase)
        except (NoSuchElementException, TimeoutException):
            self.take_screenshot('ErrorEnterText')
            utils.LOG.error(f"element was not found by {xpath}")
            pytest.fail(f"element was not found by {xpath}")

    def enter_text_by_id(self, elem_id, phrase):
        try:
            element = self.wait.until(EC.presence_of_element_located((By.ID, elem_id)))
            element.clear()
            element.send_keys(phrase)
        except (NoSuchElementException, TimeoutException):
            self.take_screenshot('ErrorEnterText')
            utils.LOG.error(f"element was not found by {elem_id}")
            pytest.fail(f"element was not found by {elem_id}")

    def get_text_by_css(self, elem_css_selector):
        try:
            element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, elem_css_selector)))
            return element.text
        except (NoSuchElementException, TimeoutException):
            self.take_screenshot('ErrorGetText')
            utils.LOG.error(f"element was not found by {elem_css_selector}")
            pytest.fail(f"element was not found by {elem_css_selector}")

    def take_screenshot(self, phrase=""):
        filepath = f"{utils.ROOT_DIR}/screenshots/{phrase}{utils.get_timestamp()}.png"
        self.driver.save_screenshot(filepath)
        utils.LOG.info(f"screenshot is taken :{filepath}")

    def get_page_by_current_url(self):
        url = self.driver.current_url
        page = url.split('/')[-1]
        page_name = page.split('.')[0]
        return page_name
