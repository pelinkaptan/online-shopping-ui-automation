import logging

from selenium.common.exceptions import NoSuchElementException
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    def login(self, email, password):
        """
      User log in
      :param email: The user email
      :param password: The user password
       """
        try:
            # Get email field
            email_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(LoginPageLocators.EMAIL_INPUT))
            if not email_field:
                raise NoSuchElementException(f"No email field found on the page")
            # Enter email
            email_field.send_keys(email)
            # Get password field
            password_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(LoginPageLocators.PASSWORD_INPUT))
            if not password_field:
                raise NoSuchElementException(f"No password field found on the page")
            # Enter password
            password_field.send_keys(password)
            # Click login button
            login_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON))
            login_btn.click()
        except Exception as e:
            logging.exception("CAUGHT AN ERROR" + str(e))
