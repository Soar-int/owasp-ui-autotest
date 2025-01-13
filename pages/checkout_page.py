import re
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Config as Config
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutPage(BasePage):
    # locators
    add_new_address_button_xpath = '//button[@aria-label="Add a new address"]'
    country_input_xpath = '//input[@data-placeholder="Please provide a country."]'
    name_input_xpath = '//input[@data-placeholder="Please provide a name."]'
    mobile_number_input_xpath = '//input[@data-placeholder="Please provide a mobile number."]'
    zip_code_input_xpath = '//input[@data-placeholder="Please provide a ZIP code."]'
    address_field_xpath = '//textarea[@data-placeholder="Please provide an address."]'
    city_input_xpath = '//input[@data-placeholder="Please provide a city."]'
    state_input_xpath = '//input[@data-placeholder="Please provide a state."]'
    submit_button_xpath = '//span[contains(text(), "Submit")]'
    address_choosing_radiobutton_xpath = '//mat-radio-button[@class="mat-radio-button mat-accent"]'
    continue_to_proceed_to_payment_button_xpath = '//button[@aria-label="Proceed to payment selection"]'
    continue_to_proceed_to_delivery_button_xpath = '//button[@aria-label="Proceed to delivery method selection"]'
    wallet_total_xpath = '//span[@class="confirmation card-title"]'
    expand_button_xpath = '//mat-panel-description[contains(text(), "Add a credit or debit card")]'
    card_name_input_xpath = '//div[@class="mat-form-field-infix ng-tns-c21-31"]/input'
    card_number_input_xpath = '//div[@class="mat-form-field-infix ng-tns-c21-32"]/input'
    expiry_month_dropdown_xpath = '//div[@class="mat-form-field-infix ng-tns-c21-11"]/select'
    expiry_month_dropdown_options_xpath = '//div[@class="mat-form-field-infix ng-tns-c21-11"]/select/option'
    expiry_year_dropdown_xpath = '//div[@class="mat-form-field-infix ng-tns-c21-12"]/select'
    expiry_year_dropdown_option_xpath = '//div[@class="mat-form-field-infix ng-tns-c21-12"]/select/option'
    confirmation_message_about_purchase_xpath = '//span[@class="mat-simple-snack-bar-content"]'

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_add_new_address_page(self):
        self.driver.find_element(By.XPATH, self.add_new_address_button_xpath).click()

    def add_new_address(self):
        self.driver.find_element(By.XPATH, self.country_input_xpath).send_keys('Armenia')
        self.driver.find_element(By.XPATH, self.name_input_xpath).send_keys('Hovhannes')
        self.driver.find_element(By.XPATH, self.mobile_number_input_xpath).send_keys(3212313213)
        self.driver.find_element(By.XPATH, self.zip_code_input_xpath).send_keys('0064')
        self.driver.find_element(By.XPATH, self.address_field_xpath).send_keys('Test-Test')
        self.driver.find_element(By.XPATH, self.city_input_xpath).send_keys('Test')
        self.driver.find_element(By.XPATH, self.state_input_xpath).send_keys('Test')
        self.driver.find_element(By.XPATH, self.submit_button_xpath).click()

    def choose_radio_button(self):
        buttons = self.driver.find_elements(By.XPATH, self.address_choosing_radiobutton_xpath)
        buttons[0].click()

    def continue_to_delivery_selection(self):
        self.driver.find_element(By.XPATH, self.continue_to_proceed_to_payment_button_xpath).click()

    def continue_to_payment_selection_selection(self):
        self.driver.find_element(By.XPATH, self.continue_to_proceed_to_delivery_button_xpath).click()

    def get_wallet_total(self):
        total = self.driver.find_element(By.XPATH, self.wallet_total_xpath).text
        return int(re.search(r'\d+', total).group())

    def expand_card_section(self):
        self.driver.find_element(By.XPATH, self.expand_button_xpath).click()

    def choose_expiry_month(self, month):
        Select(self.driver.find_element(By.ID, "mat-input-12")).select_by_value("3")

    def choose_expiry_year(self, year):
        Select(self.driver.find_element(By.ID, "mat-input-13")).select_by_value("2090")

    def fill_card_information(self):
        self.driver.find_element(By.XPATH, self.card_name_input_xpath).send_keys('Hovhannes Kasarjyan')
        self.driver.find_element(By.XPATH, self.card_number_input_xpath).send_keys(4040404040404040)
        self.choose_expiry_month(2)
        self.choose_expiry_year(2090)

    def complete_purchase(self):
        self.driver.find_element(By.XPATH, self.submit_button_xpath).click()

    def get_confirmation_message_about_purchase(self):
        text = self.driver.find_element(By.XPATH, self.confirmation_message_about_purchase_xpath).text
        return text


