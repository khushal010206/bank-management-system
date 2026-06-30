
##Bank Management System

A simple command-line bank management system built in Python with JSON-based data persistence. This project allows users to create accounts, manage their balance through deposits, withdrawals, and transfers, and update or delete their account — all secured with PIN authentication.

##Features


-Create Account — Register a new account with name, age, email, and a 4 or 6-digit PIN
-Deposit Money — Add funds to an account (with a max limit per transaction)
-Withdraw Money — Withdraw funds with balance validation
-Transfer Money — Send money from one account to another
-Show Details — View account information after PIN verification
-Update Details — Edit name, email, or PIN
-Delete Account — Permanently remove an account
-Unique Account Number Generation — Randomly generated alphanumeric account numbers with uniqueness checks
-Persistent Storage — All data is saved locally in a JSON file


##Tech Stack


-Language: Python 3
-Concepts Used: Object-Oriented Programming (OOP), class methods, encapsulation, exception handling, file I/O
-Storage: JSON


##How to Run

'''
#Clone this repository


bash - git clone https://github.com/your-username/bank-management-system.git
   cd bank-management-system


#Run the program


bash - python bank.py


#A data.json file will be created automatically on first run to store account data.
'''

##Project Structure

- bank-management-system/
  │
  ├── bank.py          # Main application file
  ├── data.json         # Auto-generated data storage (not tracked in repo)
  └── README.md         # Project documentation

##Sample Menu

========== BANK MANAGEMENT SYSTEM ==========
1. Create Account
2. Deposit Money
3. Withdraw Money
4. Transfer Money
5. Show Details
6. Update Details
7. Delete Account
8. Exit

##Future Improvements

-Hash PINs instead of storing them in plain text
-Migrate from JSON to a proper database (SQLite)
-Add transaction history logging
-Build a GUI version using Tkinter or a web interface


##Author

Khushal Kumar
