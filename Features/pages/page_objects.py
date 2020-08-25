from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webconf import Driver
from Features.helper import values


class ShopLifeCycle:

    def __init__(self):
        self.browser = Driver('firefox')

    def set_up(self):
        self.browser.nav_browser()

    def search_item(self):
        self.browser.driver.find_element_by_id(values.search_box).send_keys(values.search_word)
        self.browser.driver.find_element_by_class_name(values.search_btn).click()

    def pick_item(self):
        WebDriverWait(self.browser.driver, 60).\
            until(EC.visibility_of_element_located((By.CSS_SELECTOR, values.item_link)))
        self.browser.driver.find_element_by_css_selector(values.item_link).click()

    def add_to_cart(self):
        WebDriverWait(self.browser.driver, 60). \
            until(EC.visibility_of_element_located((By.ID, values.cart_btn)))
        self.browser.driver.find_element_by_id(values.cart_btn).click()

    def checkout(self):
        WebDriverWait(self.browser.driver, 60). \
            until(EC.visibility_of_element_located((By.ID, values.checkout_btn)))
        self.browser.driver.find_element_by_id(values.checkout_btn).click()

    def validate_page_redirect(self):
        self.browser.driver.implicitly_wait(10)
        new_page = self.browser.driver.current_url
        try:
            assert new_page == values.new_url
            print('\nPage redirect passed successfully.\n')
        except:
            raise AssertionError("Page Not Found")

    def validate_presence_(self):
        """
        The wait time was extended at a time that a very poor internet connection was experienced
        :return: It is an assertion to check the presence of a text on the page loaded.
        """
        WebDriverWait(self.browser.driver, 60).until(EC.visibility_of_element_located((By.ID, values.reviews)))
        reviews = self.browser.driver.find_element_by_id(values.reviews)
        try:
            assert values.ratings in reviews.text
            print('\nText is Present on The Page.\n')
        except:
            raise AssertionError("Error! Please Reload Page")

    def tear_down(self):
        self.browser.driver.quit()