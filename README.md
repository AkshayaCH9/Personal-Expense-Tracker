# Personal Expense Tracker

A Python-based command-line application for recording, managing, and analyzing personal expenses. The application provides features for adding, viewing, searching, summarizing, and deleting expenses, with data stored persistently in a CSV file.

## Features

* Add new expenses with amount, category, date, and description
* View all recorded expenses
* Search expenses by category
* Calculate total spending
* Generate category-wise spending summaries
* Identify the highest spending category
* Delete expenses using their unique ID
* Store and retrieve expense data using CSV files
* Validate user input and handle invalid data
* Handle file-related errors using exception handling

## Technologies Used

* **Python 3**
* **Object-Oriented Programming (OOP)**
* **CSV File Handling**
* **Exception Handling**
* **Git & GitHub**

## Project Structure

```text
personal-expense-tracker-python/
│
├── expense_tracker.py
├── expenses.csv
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/AkshayaCH9/personal-expense-tracker-python.git
```

### 2. Navigate to the project directory

```bash
cd personal-expense-tracker-python
```

### 3. Run the application

```bash
python expense_tracker.py
```

## Application Menu

```text
========================================
       PERSONAL EXPENSE TRACKER
========================================
1. Add Expense
2. View Expenses
3. Search by Category
4. Total Spending
5. Category Summary
6. Delete Expense
7. Exit
========================================
```

## Example

After adding expenses, the application can display a category-wise summary:

```text
----- CATEGORY SUMMARY -----

Food            ₹370.00
Shopping        ₹500.00
Travel          ₹80.00

Highest Spending Category: Shopping
```

## Concepts Demonstrated

This project demonstrates practical implementation of:

* Python classes and objects
* Encapsulation and object-oriented programming
* Lists and dictionaries
* Functions and methods
* File handling
* CSV data processing
* Exception handling
* Input validation
* Searching and filtering
* Data aggregation

## Future Enhancements

Possible future improvements include:

* Monthly and yearly expense reports
* Budget tracking and alerts
* Graphical user interface
* SQLite database integration
* Exporting reports to PDF
* Data visualization
* Expense editing functionality

## Author

**Akshaya**
Electronics and Communication Engineering Student
