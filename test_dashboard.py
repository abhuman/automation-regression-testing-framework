from utils.driver_factory import get_driver
from pages.dashboard_page import DashboardPage
from config.config import BASE_URL

def test_dashboard_loads():
    driver = get_driver()
    driver.get(BASE_URL)

    dashboard = DashboardPage(driver)
    assert dashboard.is_loaded()
    driver.quit()
