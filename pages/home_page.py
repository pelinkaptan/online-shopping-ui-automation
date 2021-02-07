import logging
import time

from selenium.common.exceptions import NoSuchElementException
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):

    def close_homepage_pop_up(self):
        """
       Closes female/male boutique selection pop up
       """
        time.sleep(5)
        fancy_box = self.driver.find_element(*HomePageLocators().FANCY_BOX)
        fancy_box.click()
        time.sleep(5)

    def get_all_boutique_categories_on_nav_bar(self):
        """
        Gets all boutique categories on nav bar
        :return: all boutique categories
        """
        all_categories = self.driver.find_elements(*HomePageLocators.BOUTIQUE_CATEGORY)
        return all_categories

    def check_missing_boutique_images_in_all_categories(self):
        """
         Checks missing images in all boutique categories
         :return category name and boutique name that has missing image
         """
        try:
            result = []
            all_categories = self.get_all_boutique_categories_on_nav_bar()
            for i in range(len(all_categories)):
                all_categories = self.get_all_boutique_categories_on_nav_bar()
                category_name = all_categories[i].text
                all_categories[i].click()
                missing_images = self.check_missing_boutique_images_in_a_category()
                if missing_images:
                    result.append(category_name + str(missing_images))
                self.scroll_top_of_the_page()
            return result
        except Exception as e:
            logging.exception("CAUGHT AN ERROR" + str(e))

    def check_missing_boutique_images_in_a_category(self):
        """
         Checks missing boutique images in a boutique category on home page
         :returns boutique name that has missing image
         """
        try:
            # wait until all boutiques loaded on the page
            time.sleep(2)
            self.wait_all_items_loaded()

            # get all boutiques on the page
            boutiques_found = self.get_all_elements_under_parent_element_on_page("article", "component-item")
            if not boutiques_found:
                raise NoSuchElementException(f"No boutiques found in the search page")
            # send request to check boutique image url's response code if response code is different than 200-OK,
            boutique_image_urls = [boutique.find('img').attrs['src'] for boutique in boutiques_found]

            broken_boutique_img_urls = self.check_broken_images(boutique_image_urls)

            # add boutique name into list
            if broken_boutique_img_urls:
                for broken_boutique_img_url in broken_boutique_img_urls:
                    boutiques_with_missing_img = [boutique.find('img').attrs['alt'] for boutique in boutiques_found if
                                                  broken_boutique_img_url == boutique.find('img').attrs['src']]
                    return boutiques_with_missing_img
        except Exception as e:
            logging.exception("CAUGHT AN ERROR" + str(e))

    def wait_home_page_loaded(self):
        self.wait_element_present_on_the_page(HomePageLocators.SLICK_LIST)

    def click_random_boutique(self):
        """
        Clicks random boutique on home page
        :return: boutique name
        """
        try:
            random_int = 2
            all_boutiques = self.driver.find_elements(*HomePageLocators.BOUTIQUE)
            boutique_name = all_boutiques[random_int].text
            all_boutiques[random_int].click()
            return boutique_name
        except Exception as e:
            logging.exception("CAUGHT AN ERROR" + str(e))

    def close_pop_up(self):
        notification_popup = self.driver.find_element(*HomePageLocators().NOTIFICATION_POPUP_CLOSE_BTN)
        notification_popup.click()
