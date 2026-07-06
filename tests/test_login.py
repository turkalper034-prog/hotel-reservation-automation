import time

from pages import book_hotel_page, booking_confirmation_page
from pages.book_hotel_page import BookHotelPage
from pages.booked_itinerary_page import BookedItineraryPage
from pages.booking_confirmation_page import BookingConfirmationPage
from pages.login_page import LoginPage
from pages.search_hotel_page import SearchHotelPage
from selenium.webdriver.common.by import By
from pages.select_hotel_page import SelectHotelPage


def test_login(driver):
    driver.get("https://adactinhotelapp.com/")
    login_page = LoginPage(driver)
    login_page.enter_username("Alper767511")
    login_page.enter_password("Alper200311")
    login_page.click_button()
    login_page.wait_for_search_hotel_page()
    assert "Search Hotel" in login_page.driver.title
    search_hotel_page = SearchHotelPage(driver)
    search_hotel_page.select_location("Sydney")
    search_hotel_page.select_hotel("Hotel Creek")
    search_hotel_page.select_room_type("Standard")
    search_hotel_page.select_number_of_rooms("2 - Two")
    search_hotel_page.select_adults_per_room("2 - Two")
    search_hotel_page.select_children_per_room("1 - One")
    search_hotel_page.enter_check_in_date("10/07/2026")
    search_hotel_page.enter_check_out_date("12/07/2026")
    search_hotel_page.click_search_button()
    select_hotel_page = SelectHotelPage(driver)
    select_hotel_page.select_first_hotel()
    select_hotel_page.click_continue()
    book_hotel_page = BookHotelPage(driver)
    book_hotel_page.enter_first_name("Alper")
    book_hotel_page.enter_last_name("Türk")
    book_hotel_page.enter_address("Istanbul")
    book_hotel_page.select_credit_card_type("VISA")
    book_hotel_page.enter_credit_card_number("4111111111111111")
    book_hotel_page.select_expiry_month("December")
    book_hotel_page.select_expiry_year("2030")
    book_hotel_page.enter_cvv("123")
    book_hotel_page.click_book_now()
    time.sleep(10)
    booking_confirmation_page = BookingConfirmationPage(driver)
    order_no = booking_confirmation_page.get_order_number()
    booking_confirmation_page.click_my_itinerary()
    print("ORDER_NO:", order_no)

    booked_itinerary_page = BookedItineraryPage(driver)

    booked_itinerary_page.enter_order_number(order_no)

    booked_itinerary_page.click_go_button()
    time.sleep(10)
    booked_itinerary_page.select_booking()
    time.sleep(10)
    booked_itinerary_page.click_cancel_selected()
    time.sleep(10)

    booked_itinerary_page.accept_alert()
    print("ORDER_NO:", order_no)




    time.sleep(10)



