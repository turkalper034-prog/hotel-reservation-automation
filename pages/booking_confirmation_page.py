from selenium.webdriver.common.by import By

class BookingConfirmationPage:

    order_number_input = (By.ID, "order_no")
    my_itinerary_button = (By.ID, "my_itinerary")
    def __init__(self, driver):
        self.driver = driver

    def get_order_number(self):
        return self.driver.find_element(*self.order_number_input).get_attribute("value")

    def click_my_itinerary(self):
        self.driver.find_element(*self.my_itinerary_button).click()