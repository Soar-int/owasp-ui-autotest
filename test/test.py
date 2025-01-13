import time

import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.basket_page import BasketPage
from pages.checkout_page import CheckoutPage
from config import Config as Config
from driver_manager import DriverManager


@pytest.fixture
def driver():
    driver = DriverManager.get_driver()
    yield driver
    driver.quit()


def test_open_home_page(driver):
    driver.get(Config.BASE_URL)
    assert "OWASP Juice Shop" in driver.title, "Title does not match"


def test_task_1(driver):
    driver.get(Config.BASE_URL)
    home_page = HomePage(driver)
    home_page.close_initial_popup()
    home_page.change_items_count_per_page('48')
    assert home_page.get_items_count_per_page() == '1 – 37 of 37'


def test_task_2(driver):
    driver.get(Config.BASE_URL)
    home_page = HomePage(driver)
    home_page.close_initial_popup()
    home_page.open_apple_juice_item()
    assert home_page.get_apple_juice_image().is_displayed()
    home_page.expand_review_section()
    time.sleep(5)
    home_page.close_item_popup()


def test_task_3(driver):
    driver.get(Config.BASE_URL)
    home_page = HomePage(driver)
    home_page.close_initial_popup()
    home_page.navigate_to_login_page()
    login_page = LoginPage(driver)
    login_page.navigate_to_registration_page()
    registration_page = RegistrationPage(driver)
    assert registration_page.get_email_field_validation_message() == 'Please provide an email address.', \
        'Validation Message does not appear'
    assert registration_page.get_password_field_validation_message() == 'Please provide a password.', \
        'Validation Message does not appear'
    assert registration_page.get_repeat_password_field_validation_message() == 'Please repeat your password.', \
        'Validation Message does not appear'
    assert registration_page.get_security_question_field_validation_message() == 'Please select a security question.', \
        'Validation Message does not appear'
    assert registration_page.get_answer_field_validation_message() == \
           'Please provide an answer to your security question.', 'Validation message does not appear'
    registration_page.fill_all_data()
    registration_page.press_register_button()
    assert login_page.get_registration_successful_message() == \
           'Registration completed successfully. You can now log in.', 'Confirmation message does not appear'
    login_page.user_login()


def test_task_4(driver):
    driver.get(Config.BASE_URL)
    home_page = HomePage(driver)
    home_page.close_initial_popup()
    home_page.navigate_to_login_page()
    login_page = LoginPage(driver)
    login_page.user_login()
    home_page.add_5_items_to_basket()
    time.sleep(1)
    assert home_page.get_basket_items_count() == 5
    home_page.navigate_to_your_basket()
    time.sleep(1)
    basket_page = BasketPage(driver)
    initial_total = basket_page.get_basket_total()
    basket_page.increase_item_count()
    basket_page.delete_item_from_basket()
    time.sleep(1)
    current_total = basket_page.get_basket_total()
    assert initial_total != current_total
    time.sleep(5)
    basket_page.navigate_to_checkout_page()
    checkout_page = CheckoutPage(driver)
    checkout_page.navigate_to_add_new_address_page()
    checkout_page.add_new_address()
    checkout_page.choose_radio_button()
    checkout_page.continue_to_delivery_selection()
    checkout_page.choose_radio_button()
    checkout_page.continue_to_payment_selection_selection()
    time.sleep(1)
    assert checkout_page.get_wallet_total() == 0.00
    checkout_page.expand_card_section()
    checkout_page.fill_card_information()
    checkout_page.complete_purchase()
    assert checkout_page.get_confirmation_message_about_purchase()



