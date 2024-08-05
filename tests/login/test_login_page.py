import pytest
from core.ui.chrome_driver_manager import ChromeDriverManager
from main.ui.base_page import BasePage
import config

def test_login():
    driver = ChromeDriverManager.get_chrome_driver()
    base_page = BasePage(driver)
    base_page.navigate_to(config.BASE_URL)
    titulo = driver.title
    print(f"Título de la página: {titulo}")
    driver.quit()
