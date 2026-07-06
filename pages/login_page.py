import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginPage:
    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login")
    search_hotel_title = (By.CLASS_NAME, "login_title")
    def __init__(self,driver):
        self.driver = driver

    def enter_username(self,username):
        self.driver.find_element(*self.username_input).send_keys(username)
    def enter_password(self,password):
        self.driver.find_element(*self.password_input).send_keys(password)
    def click_button(self):
        self.driver.find_element(*self.login_button).click()
        time.sleep(10)
    def wait_for_search_hotel_page(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((self. search_hotel_title)))
    def get_page_title(self):
        text = self.driver.find_element(*self.search_hotel_title).text
        print(text)
        return text


