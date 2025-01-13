from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class DriverManager:
    @staticmethod
    def get_driver():
        options = Options()
        options.add_argument("--start-maximized")
        # Use ChromeDriverManager to manage chromedriver installation
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver
