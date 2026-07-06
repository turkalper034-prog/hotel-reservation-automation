from selenium.webdriver.common.by import By

class SelectHotelPage:
    selected_hotel_radio = (By.ID, "radiobutton_0")
    continue_button = (By.ID, "continue")

    def __init__(self, driver):
        self.driver = driver

    def select_first_hotel(self):
        self.driver.find_element(*self.selected_hotel_radio).click()

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()