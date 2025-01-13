import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Config as Config
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BasketPage(BasePage):
    # locators
    total_price_xpath = '//div[@id="price"]'
    checkout_button_xpath = '//button[@id="checkoutButton"]'
    x_icon_xpath = '//button[@class="mat-focus-indicator mat-button mat-button-base"]'

    def __init__(self, driver):
        super().__init__(driver)

    def get_plus_button(self, product_name):
        xpath = f"//mat-cell[contains(text(), '{product_name}')]/following-sibling::mat-cell//button[2]/span[1]"
        return self.driver.find_element(By.XPATH, xpath)

    def get_basket_total(self):
        total = self.driver.find_element(By.XPATH, self.total_price_xpath).text
        return float(re.search(r'\d+', total).group())

    def increase_item_count(self):
        for i in range(3):
            self.get_plus_button('Apple Juice').click()

    def get_delete_button(self, product_name):
        xpath = f"//mat-cell[contains(text(), '{product_name}')]/following-sibling::mat-cell//button[1]"
        buttons = self.driver.find_elements(By.XPATH, xpath)
        buttons[1].click()

    def delete_item_from_basket(self):
        self.get_delete_button('Apple Juice')

    def navigate_to_checkout_page(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.checkout_button_xpath).click()


