import logging
import time
import random

from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from requests_toolbelt.threaded import pool


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def wait_page_loading(self):
        attempt_page_load = 0
        page_state = 'not complete'
        while page_state != 'complete' and attempt_page_load <= 20:
            page_state = self.driver.execute_script('return document.readyState;')
            time.sleep(1)
            attempt_page_load = attempt_page_load + 1

    def wait_element_present_on_the_page(self, element):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(element))

    def wait_all_items_loaded(self):
        self.wait_page_loading()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        page_loading = True
        while page_loading:
            # get page url
            page_url1 = self.driver.current_url
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(2)
            # get page url again
            page_url2 = self.driver.current_url
            if page_url1 == page_url2:
                page_loading = False

    def scroll_top_of_the_page(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def click_random_element_by_locator(self, locator):
        """
        Clicks random item on the page
        :param locator: element locator
        :return: item name
        """
        try:
            random_int = random.randint(0, 9)
            all_items = self.driver.find_elements(*locator)
            all_items[random_int].click()

        except Exception as e:
            logging.exception("CAUGHT AN ERROR" + str(e))

    def check_broken_images(self, image_urls):
        """
        Checks image urls responses
        :param image_urls: list of urls
        :return: list of broken images
        """
        try:
            p = pool.Pool.from_urls(image_urls)
            p.join_all()
            broken_img_urls = [response.request_kwargs['url'] for response in p.responses() if
                               response.status_code != 200 or 'placeholder.jpg' in response.request_kwargs[
                                   'url']]
            return broken_img_urls
        except Exception as e:
            logging.exception("CAUGHT AN ERROR" + str(e))

    def get_all_elements_under_parent_element_on_page(self, tag_name, css_class):
        """
        Gets all elements under parent element on the page using web scrapping
        :return: list of the elements
        """
        try:
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            items_found = soup.find_all(tag_name, class_=css_class)
            return items_found
        except Exception as e:
            logging.exception("CAUGHT AN ERROR" + str(e))

    def click_element_by_locator(self, locator):
        """
        Clicks element by locator
        """
        element = self.driver.find_element(*locator)
        element.click()
