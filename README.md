# 🧓 ElderAid — Django-Based Elder Care Service Platform

ElderAid is a web application built using Django and PostgreSQL that allows users to explore elder care services and subservices freely, and log in only when booking. Designed to provide a smooth and user-friendly experience, especially for elderly users or their caretakers.

---

## 🚀 Features

- 🆓 Publicly browse services and subservices
- 🔐 Custom login/signup system (session-based)
- 📅 Booking with `from_date` and `to_date` → auto-calculates total price
- 🧮 Price = subservice_price × number of days
- 📥 Bookings history (for logged-in users only)
- 💻 Responsive Bootstrap 5 UI
- ☁️ PostgreSQL database support

---

## 🛠 Tech Stack

| Tech       | Used For                 |
|------------|--------------------------|
| Python 3   | Programming Language     |
| Django     | Web Framework            |
| PostgreSQL | Relational Database      |
| Bootstrap 5| Frontend & Styling       |
| HTML/CSS   | Templates                |
| jQuery     | AJAX Page Transitions    |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/elderaid.git
cd elderaid
