# 🏨 Hotel Reservation Automation

A Selenium-based test automation framework developed with **Python**, **Pytest**, and the **Page Object Model (POM)** design pattern.

This project automates the complete hotel reservation workflow on the Adactin Hotel Application, from login to booking cancellation.

---

## 🚀 Technologies Used

* Python
* Selenium WebDriver
* Pytest
* Page Object Model (POM)
* ChromeDriver

---

## 📁 Project Structure

```
hotel-reservation-automation/
│
├── pages/
│   ├── login_page.py
│   ├── search_hotel_page.py
│   ├── select_hotel_page.py
│   ├── book_hotel_page.py
│   ├── booking_confirmation_page.py
│   └── booked_itinerary_page.py
│
├── tests/
│   └── test_login.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

---

## ✅ Automated Test Flow

The automation performs the following steps:

1. Launches Chrome browser
2. Opens the Adactin Hotel Application
3. Logs in with a valid user
4. Searches for a hotel
5. Selects the first available hotel
6. Completes the booking form
7. Creates a reservation
8. Retrieves the generated Order Number
9. Opens the Booked Itinerary page
10. Searches for the booking using the Order Number
11. Cancels the booking
12. Confirms the cancellation alert

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/hotel-reservation-automation.git
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the test:

```bash
pytest
```

---

## 🧩 Design Pattern

This project follows the **Page Object Model (POM)** design pattern.

Each web page has its own class that contains:

* Locators
* Page actions
* Utility methods

This approach keeps the test code clean, reusable, and easy to maintain.

---

## 🎯 Test Scenario

* Login
* Search Hotel
* Select Hotel
* Book Hotel
* Capture Order Number
* Search Booking
* Cancel Booking
* Verify successful execution

---

## 👨‍💻 Author

**Alper Türk**
