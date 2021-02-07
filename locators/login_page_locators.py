"""Login Page Locators"""
from selenium.webdriver.common.by import By


class LoginPageLocators:

    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-testid='email-input']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-testid='password-input']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
