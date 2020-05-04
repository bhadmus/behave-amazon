from selenium import webdriver


class Driver:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def nav_browser(self):

        self.driver.get("https://www.amazon.com/")
        # self.driver.maximize_window()



