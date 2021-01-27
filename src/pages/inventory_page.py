import time

import pytest
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

from src.pages.base_page import BasePage
import src.utilities as utils


class InventoryPage(BasePage):
    """
    Page factory for Products page
    """
    # Locators
    sort_dropdown_class = "product_sort_container"
    shopping_cart_xpath = "//div[@id='shopping_cart_container']/a"

    # Methods
    @property
    def get_page_title(self):
        return self.driver.title

    def sort_products_by(self, option):

        try:
            utils.LOG.info(f"sorting product by {option} ...")
            element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.sort_dropdown_class)))
            drop_down = Select(element)
            drop_down.select_by_visible_text(option)

            self.take_screenshot('SortProductsBySelected')
            utils.LOG.info(f"Product sorted by {option}.")

        except (NoSuchElementException, TimeoutException):
            self.take_screenshot('ErrorSortProductsBy')
            utils.LOG.error(f"sort product by {option} failed.")
            pytest.fail(f"sort product by {option} failed.")

    def add_to_cart_by_prod_name(self, product_name):
        button_xpath = f"//div[@class='inventory_item_name' and text()='{product_name}']/../../..//button[text()='ADD TO CART']"
        self.click_element_by_xpath(button_xpath)
        utils.LOG.info(f"product {product_name} is added to cart.")

    def remove_by_prod_name(self, product_name):
        button_xpath = f"//div[@class='inventory_item_name' and text()='{product_name}']/../../..//button[text()='REMOVE']"
        self.click_element_by_xpath(button_xpath)
        utils.LOG.info(f"product {product_name} is removed from cart.")

    def get_price_by_prod_name(self, product_name):
        pass

    def get_desc_by_prod_name(self, product_name):
        pass

    def open_shopping_cart(self):
        utils.LOG.info(f"Opening the shopping card.")
        self.click_element_by_xpath(self.shopping_cart_xpath)
        time.sleep(5)
