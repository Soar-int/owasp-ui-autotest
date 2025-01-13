from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Config as Config
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    # locators
    not_yet_a_customer_textlink_xpath = '//div[@id="newCustomerLink"]'
    email_field_xpath = '//input[@id="email"]'
    password_field_xpath = '//input[@id="password"]'
    login_button_xpath = '//button[@id="loginButton"]'
    registration_message_xpath = '//span[@class="mat-simple-snack-bar-content"]'

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_registration_page(self):
        self.driver.find_element(By.XPATH, self.not_yet_a_customer_textlink_xpath).click()

    def user_login(self):
        self.driver.find_element(By.XPATH, self.email_field_xpath).send_keys(Config.EMAIL)
        self.driver.find_element(By.XPATH, self.password_field_xpath).send_keys(Config.PASSWORD)
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def get_registration_successful_message(self):
        WebDriverWait(self.driver, Config.IMPLICIT_WAIT).until(EC.presence_of_element_located((
            By.XPATH, self.registration_message_xpath)))
        message = self.driver.find_element(By.XPATH, self.registration_message_xpath).text
        return message
