from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class GooglePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.search_box = (By.NAME, "q")

    def open(self):
        self.driver.get("https://www.google.com")

    def search(self, term):
        search_box = self.driver.find_element(*self.search_box)
        search_box.send_keys(term)
        search_box.submit()

    def get_results_title(self):
        return self.driver.title
