
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.page_objects.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(SearchPage, self).__init__(driver, wait_driver)

    def searchnew(self, value: str):
        self.element("search_new").wait_clickable().send_keys(value)
        self.element("search_btn").wait_clickable().click()
