from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Config as Config
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    # locators
    initial_popup_xpath = '//button[@color="primary"]'
    dropdown_xpath = '//mat-select[@id="mat-select-0"]'
    dropdown_options_xpath = '//span[@class="mat-option-text"]'
    items_count_xpath = '//div[@class="mat-paginator-range-label"]'
    apple_juice_xpath = '//div[contains(text(), " Apple Juice (1000ml) ")]'
    apple_juice_image_xpath = '//img[@class="img-thumbnail"]'
    review_section_path = '//mat-expansion-panel-header[@role="button"]'
    close_button_xpath = '//button[@mat-dialog-close=""]'
    account_xpath = '//button[@id="navbarAccount"]'
    login_button_xpath = '//button[@id="navbarLoginButton"]'
    add_to_basket_button_xpath = '//span[contains(text(), "Add to Basket")]'
    your_basket_button_xpath = '//button[@routerlink="/basket"]'
    added_items_confirmation_massage = '//span[@class="mat-simple-snack-bar-content"]'
    basket_items_count_xpath = '//span[@class="fa-layers-counter fa-layers-top-right fa-3x warn-notification"]'

    def __init__(self, driver):
        super().__init__(driver)

    def close_initial_popup(self):
        WebDriverWait(self.driver, Config.IMPLICIT_WAIT).until(EC.presence_of_element_located((
            By.XPATH, self.initial_popup_xpath)))
        self.driver.find_element(By.XPATH, self.initial_popup_xpath).click()

    def change_items_count_per_page(self, value_to_select):
        dropdown = self.driver.find_element(By.XPATH, self.dropdown_xpath)
        dropdown.click()
        options = self.driver.find_elements(By.XPATH, self.dropdown_options_xpath)
        for option in options:
            if option.text == str(value_to_select):
                option.click()
                break

    def get_items_count_per_page(self):
        return self.driver.find_element(By.XPATH, self.items_count_xpath).text

    def open_apple_juice_item(self):
        self.driver.find_element(By.XPATH, self.apple_juice_xpath).click()

    def get_apple_juice_image(self):
        return self.driver.find_element(By.XPATH, self.apple_juice_image_xpath)

    def expand_review_section(self):
        self.driver.find_element(By.XPATH, self.review_section_path).click()

    def close_item_popup(self):
        self.driver.find_element(By.XPATH, self.close_button_xpath).click()

    def navigate_to_login_page(self):
        self.driver.find_element(By.XPATH, self.account_xpath).click()
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def add_5_items_to_basket(self):
        WebDriverWait(self.driver, Config.IMPLICIT_WAIT).until(EC.presence_of_element_located((
            By.XPATH, self.add_to_basket_button_xpath)))
        elements = self.driver.find_elements(By.XPATH, self.add_to_basket_button_xpath)
        for element in elements[:6]:
            element.click()
            assert WebDriverWait(self.driver, Config.IMPLICIT_WAIT).until(EC.presence_of_element_located((
                By.XPATH, self.added_items_confirmation_massage)))

    def navigate_to_your_basket(self):
        WebDriverWait(self.driver, Config.IMPLICIT_WAIT).until(EC.presence_of_element_located((
            By.XPATH, self.your_basket_button_xpath)))
        self.driver.find_element(By.XPATH, self.your_basket_button_xpath).click()

    def get_basket_items_count(self):
        count = self.driver.find_element(By.XPATH, self.basket_items_count_xpath).text
        return int(count)
