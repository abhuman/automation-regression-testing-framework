from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    HEADER = (By.TAG_NAME, "h1")

    def is_loaded(self):
        return self.wait_for_element(self.HEADER).is_displayed()
