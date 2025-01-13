import time

from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Config as Config
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RegistrationPage(BasePage):
    # locators
    user_registration_icon_xpath = '//h1[contains(text(), "User Registration")]'
    email_field_xpath = '//input[@id="emailControl"]'
    email_field_validation_message_xpath = '//mat-error[@id="mat-error-2"]'
    password_field_xpath = '//input[@id="passwordControl"]'
    password_field_validation_message_xpath = '//mat-error[@id="mat-error-3"]'
    repeat_password_field_xpath = '//input[@id="repeatPasswordControl"]'
    repeat_password_field_validation_message_xpath = '//mat-error[@id="mat-error-4"]'
    security_question_xpath = '//div[@id="mat-select-value-3"]'
    security_question_options_xpath = '//span[@class="mat-option-text"]'
    security_question_field_validation_message_xpath = '//mat-error[@id="mat-error-5"]'
    answer_field_xpath = '//input[@id="securityAnswerControl"]'
    answer_field_validation_message_xpath = '//mat-error[@id="mat-error-6"]'
    register_button = '//button[@id="registerButton"]'
    show_password_advice = '//span[@class="mat-slide-toggle-bar"]'

    def __init__(self, driver):
        super().__init__(driver)

    def get_email_field_validation_message(self):
        self.driver.find_element(By.XPATH, self.email_field_xpath).click()
        self.driver.find_element(By.XPATH, self.user_registration_icon_xpath).click()
        time.sleep(1)
        text = self.driver.find_element(By.XPATH, self.email_field_validation_message_xpath).text
        return text

    def get_password_field_validation_message(self):
        self.driver.find_element(By.XPATH, self.password_field_xpath).click()
        self.driver.find_element(By.XPATH, self.user_registration_icon_xpath).click()
        time.sleep(1)
        text = self.driver.find_element(By.XPATH, self.password_field_validation_message_xpath).text
        return text

    def get_repeat_password_field_validation_message(self):
        self.driver.find_element(By.XPATH, self.repeat_password_field_xpath).click()
        self.driver.find_element(By.XPATH, self.user_registration_icon_xpath).click()
        time.sleep(1)
        text = self.driver.find_element(By.XPATH, self.repeat_password_field_validation_message_xpath).text
        return text

    def get_security_question_field_validation_message(self):
        self.driver.find_element(By.XPATH, self.security_question_xpath).click()
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
        time.sleep(1)
        text = self.driver.find_element(By.XPATH, self.security_question_field_validation_message_xpath).text
        return text

    def get_answer_field_validation_message(self):
        self.driver.find_element(By.XPATH, self.answer_field_xpath).click()
        self.driver.find_element(By.XPATH, self.user_registration_icon_xpath).click()
        time.sleep(1)
        text = self.driver.find_element(By.XPATH, self.answer_field_validation_message_xpath).text
        return text

    def give_email(self):
        self.driver.find_element(By.XPATH, self.email_field_xpath).send_keys(Config.EMAIL)

    def give_password(self):
        self.driver.find_element(By.XPATH, self.password_field_xpath).send_keys(Config.PASSWORD)

    def give_repeat_password(self):
        self.driver.find_element(By.XPATH, self.repeat_password_field_xpath).send_keys(Config.PASSWORD)

    def choose_security_question(self, value_to_select):
        dropdown = self.driver.find_element(By.XPATH, self.security_question_xpath)
        dropdown.click()
        options = self.driver.find_elements(By.XPATH, self.security_question_options_xpath)
        for option in options:
            if option.text == str(value_to_select):
                option.click()
                break

    def give_an_answer(self):
        self.driver.find_element(By.XPATH, self.answer_field_xpath).send_keys(Config.ANSWER)

    def fill_all_data(self):
        self.give_email()
        self.give_password()
        self.give_repeat_password()
        self.driver.find_element(By.XPATH, self.show_password_advice).click()
        self.choose_security_question(Config.SECURITY_QUESTION)
        self.give_an_answer()

    def press_register_button(self):
        self.driver.find_element(By.XPATH, self.register_button).click()
