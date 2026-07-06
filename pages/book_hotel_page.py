from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class BookHotelPage:
    first_name_input = (By.ID, 'first_name')
    last_name_input = (By.ID, "last_name")
    address_input = (By.ID, "address")
    credit_card_input = (By.ID, "cc_num")
    credit_card_type_dropdown = (By.ID, "cc_type")
    expiry_month_dropdown = (By.ID, "cc_exp_month")
    expiry_year_dropdown = (By.ID, "cc_exp_year")
    cvv_input = (By.ID, "cc_cvv")
    book_now_button = (By.ID, "book_now")


    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self,first_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    def enter_address(self, address):
        self.driver.find_element(*self.address_input).send_keys(address)

    def select_credit_card_type(self, cc_type):
        dropdown = Select(self.driver.find_element(*self.credit_card_type_dropdown))
        dropdown.select_by_visible_text(cc_type)
    def click_book_now(self):
        self.driver.find_element(*self.book_now_button).click()

    def enter_credit_card_number(self, card_number):
        self.driver.find_element(*self.credit_card_input).send_keys(card_number)


    def select_expiry_month(self, month):
         dropdown = Select(self.driver.find_element(*self.expiry_month_dropdown))
         dropdown.select_by_visible_text(month)

    def select_expiry_year(self, year):
        dropdown = Select(self.driver.find_element(*self.expiry_year_dropdown))
        dropdown.select_by_visible_text(year)

    def enter_cvv(self, cvv):
        self.driver.find_element(*self.cvv_input).send_keys(cvv)


    def wait_for_book_hotel_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name_input))





