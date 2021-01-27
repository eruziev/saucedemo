import pytest
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

from src.pages.base_page import BasePage
import src.utilities as utils


class CartPage(BasePage):
    """
    Page factory for Cart page
    """
    # Locators
    sort_dropdown_class = "product_sort_container"
    shopping_cart_xpath = "//div[@id='shopping_cart_container']/a"
    product_name_css = "div.inventory_item_name"
    continue_shopping = "//a[contains(text(),'Continue Shopping')]"
    checkout_button = "//a[contains(text(),'CHECKOUT')]"

    # Methods
    @property
    def get_page_title(self):
        return self.driver.title

    def click_product_by_name(self, product_name):
        utils.LOG.info(f"clicking the product {product_name} to view.")
        item_link_xpath = f"//div[@class='inventory_item_name' and text()='{product_name}']"
        self.click_element_by_xpath(item_link_xpath)

    def remove_by_prod_name(self, product_name):
        button_xpath = f"//div[@class='inventory_item_name' and text()='{product_name}']/../../..//button[text()='REMOVE']"
        self.click_element_by_xpath(button_xpath)
        utils.LOG.info(f"product {product_name} is removed from cart.")

    def get_product_name_list(self):
        elements = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.product_name_css)))
        names = []
        for element in elements:
            names.append(element.text)
        return names

    def get_price_by_prod_name(self, product_name):
        pass

    def get_desc_by_prod_name(self, product_name):
        pass

    def click_continue_shopping(self):
        self.click_element_by_xpath(self.continue_shopping)
        utils.LOG.info(f"Continue shopping is clicked.")

    def click_checkout(self):
        self.click_element_by_xpath(self.checkout_button)
        utils.LOG.info(f"checkout button is clicked.")


class CheckoutPage(BasePage):
    """
    Page factory for Checkout step 1, step 2
    """
    first_name_id = "first-name"
    last_name_id = "last-name"
    zip_code_id = "postal-code"
    cancel_button = ""
    continue_button = "//input[@value='CONTINUE']"
    finish_button = "//a[text()='FINISH']"
    product_name_css = "div.inventory_item_name"
    total_css = "div.summary_total_label"
    subtotal_css = "div.summary_subtotal_label"

    def enter_first_name(self, first_name):
        self.enter_text_by_id(self.first_name_id, first_name)
        utils.LOG.info(f"first name entered: {first_name}")

    def enter_last_name(self, last_name):
        self.enter_text_by_id(self.last_name_id, last_name)
        utils.LOG.info(f"last name entered: {last_name}")

    def enter_zip_code(self, zip_code):
        self.enter_text_by_id(self.zip_code_id, zip_code)
        utils.LOG.info(f"zip code entered: {zip_code}")

    def click_continue(self):
        self.click_element_by_xpath(self.continue_button)
        utils.LOG.info(f"Continue button clicked, continue to checkout.")

    def click_finish(self):
        self.click_element_by_xpath(self.finish_button)
        utils.LOG.info(f"finish button clicked on checkout.")

    def click_cancel(self):
        pass

    def get_product_name_list(self):
        elements = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.product_name_css)))
        names = []
        for element in elements:
            names.append(element.text)
        return names

    def get_total_amount(self):
        msg = self.get_text_by_css(self.total_css)
        amount = msg.split('$')[-1]
        return float(amount)

    def get_subtotal_amount(self):
        msg = self.get_text_by_css(self.subtotal_css)
        amount = msg.split('$')[-1]
        return float(amount)

    def get_price_by_prod_name(self, product_name):
        pass
        # return float(amount)
