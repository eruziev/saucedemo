from src.pages.base_page import BasePage


class Login(BasePage):
    """
    Page factory for Login page: Elements and functions for actions.
    Inherited a driver from base page.
    """
    # LOCATORS
    username_box = "//input[@id='user-name']"
    password_box = "//input[@id='password']"
    login_button_id = "login-button"

    # ACTIONS ON THE PAGE
    def enter_username(self, username):
        self.enter_text_by_xpath(self.username_box, username)

    def enter_password(self, phrase):
        self.enter_text_by_xpath(self.password_box, phrase)

    def click_login(self):
        self.click_element_by_id(self.login_button_id)

    @property
    def get_page_title(self):
        return self.driver.title
