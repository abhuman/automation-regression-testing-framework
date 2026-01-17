from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from config.config import BASE_URL
from utils.test_data import VALID_USER

def test_valid_login():
    driver = get_driver()
    driver.get(BASE_URL)

    login = LoginPage(driver)
    login.login(VALID_USER["username"], VALID_USER["password"])

    assert "Dashboard" in driver.title
    driver.quit()
