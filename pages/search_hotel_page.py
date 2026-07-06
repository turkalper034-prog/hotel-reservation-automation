from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class SearchHotelPage:
    location_dropdown = (By.ID, "location")
    hotels_dropdown = (By.ID, "hotels")
    room_type_dropdown = (By.ID, "room_type")
    number_of_rooms_dropdown = (By.ID, "room_nos")
    adults_per_room_dropdown = (By.ID, "adult_room")
    children_per_room_dropdown = (By.ID, "child_room")
    check_in_date_input = (By.ID, "datepick_in")
    check_out_date_input = (By.ID, "datepick_out")
    search_button = (By.ID, "Submit")

    def __init__(self, driver):
        self.driver = driver

    def select_location(self,location):
        dropdown = Select(self.driver.find_element(*self.location_dropdown))
        dropdown.select_by_visible_text(location)

    def select_hotel(self,hotel):
        dropdown = Select(self.driver.find_element(*self.hotels_dropdown))
        dropdown.select_by_visible_text(hotel)

    def select_room_type(self,room_type):
        dropdown = Select(self.driver.find_element(*self.room_type_dropdown))
        dropdown.select_by_visible_text(room_type)

    def select_number_of_rooms(self, rooms):
        dropdown = Select(self.driver.find_element(*self.number_of_rooms_dropdown))
        dropdown.select_by_visible_text(rooms)

    def select_adults_per_room(self, adults):
        dropdown = Select(self.driver.find_element(*self.adults_per_room_dropdown))
        dropdown.select_by_visible_text(adults)


    def select_children_per_room(self, children):
        dropdown = Select(self.driver.find_element(*self.children_per_room_dropdown))
        dropdown.select_by_visible_text(children)

    def enter_check_in_date(self, check_in_date):
        self.driver.find_element(*self.check_in_date_input).clear()
        self.driver.find_element(*self.check_in_date_input).send_keys(check_in_date)

    def enter_check_out_date(self, check_out_date):
        self.driver.find_element(*self.check_out_date_input).clear()
        self.driver.find_element(*self.check_out_date_input).send_keys(check_out_date)

    def click_search_button(self):
        self.driver.find_element(*self.search_button).click()
