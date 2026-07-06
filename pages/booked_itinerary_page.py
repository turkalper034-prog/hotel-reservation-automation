from selenium.webdriver.common.by import By

class BookedItineraryPage:

    search_order_input = (By.ID, "order_id_text")
    go_button = (By.ID, "search_hotel_id")
    order_checkbox = (By.NAME, "ids[]")
    cancel_selected_button = (By.NAME, "cancelall")


    def __init__(self, driver):
        self.driver = driver

    def enter_order_number(self, order_no):
        self.driver.find_element(*self.search_order_input).send_keys(order_no)

    def click_go_button(self):
        self.driver.find_element(*self.go_button).click()

    def select_booking(self):
        self.driver.find_element(*self.order_checkbox).click()

    def click_cancel_selected(self):
        self.driver.find_element(*self.cancel_selected_button).click()


    def accept_alert(self):
        self.driver.switch_to.alert.accept()