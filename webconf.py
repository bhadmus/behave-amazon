from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from Features.helper import values


class Driver:
    """
    This class can, and will be modified soon to allow different web driver
    options like Firefox, Safari, or Edge
    """

    def __init__(self, browser_type=None):
        if not browser_type:

            self.driver = webdriver.Chrome()

        elif browser_type.lower() == 'firefox':

            cap = DesiredCapabilities().FIREFOX
            cap["marionette"] = False
            firefox_options = FOptions()
            firefox_options.add_argument("--headless")
            self.driver = webdriver.Firefox(capabilities=cap, options=firefox_options)
            # self.driver = webdriver.Firefox()


        else:
            raise NameError(f'{browser_type} is not accepted.')

    def nav_browser(self):
        """
        This navigates to the e-commerce site
        :return:
        """

        self.driver.get(values.parent_url)
