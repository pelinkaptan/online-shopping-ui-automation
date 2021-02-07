import logging

from selenium.common.exceptions import NoSuchElementException
import time

from pages.base_page import BasePage


class BoutiqueDetail(BasePage):

    def check_missing_images_in_a_boutique(self):
        """
         Checks missing images in a boutique detail page
         :returns item img url
         """
        try:
            # wait until all items in the boutique loaded
            time.sleep(2)
            self.wait_all_items_loaded()

            # get all items in the boutique
            items_found = self.get_all_elements_under_parent_element_on_page("div", "image-container")
            if not items_found:
                raise NoSuchElementException(f"No items found in the boutique page" + self.driver.current_url)
            # send request to check image url's response code if response code is different than 200-OK,
            item_image_urls = [item.find('img').attrs['src'] for item in items_found]

            broken_item_img_urls = self.check_broken_images(item_image_urls)
            return broken_item_img_urls
        except Exception as e:
            logging.exception("CAUGHT AN ERROR" + str(e))
