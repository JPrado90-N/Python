from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class ChromeDriverManager:
    @staticmethod
    def get_chrome_driver():
        # This is the correct way to use ChromeDriverManager with webdriver_manager
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        return driver
