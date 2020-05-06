from selenium import webdriver
from Features.helper import values


class Driver:
    """
    This class can and will be modidfied soon to allow different web driver options like Firefox, Safari, or Edge
    """

    def __init__(self):
        self.driver = webdriver.Chrome()

    def nav_browser(self):
        """
        This navigates to the e-commerce site
        :return:
        """

        self.driver.get(values.parent_url)