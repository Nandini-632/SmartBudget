# SmartBudget

An interactive command-line budgeting application built in Python that helps users track their monthly income, log categorized expenses, and view a detailed financial summary.

Project Overview:
SmartBudget is a lightweight financial tool designed to simplify personal budget tracking. Users can input their total monthly income and dynamically log multiple expenses under specific categories (e.g., food, rent, entertainment). The system continuously aggregates the data to provide an instant health check on the user's spending habits, alerting them if they are overspending or hitting their financial goals.

Features:
Dynamic Expense Logging: Enter multiple expenses continuously until you type 'done'.
Smart Aggregation: Automatically groups and sums duplicate categories (e.g., entering 'food' multiple times combines the total).
Input Validation: Error handling protects against invalid inputs like alphabetic characters or negative financial numbers.
Financial Health Alerts: Instantly flags if you have exceeded your budget or spent 100% of your cash.
Formatted Outputs: Cleans up currency calculations using proper decimal formatting (`.2f`).

Technologies & Tools Used:
Language: Python 3.x
Core Concepts: Modular programming, Exception handling (`try-except`), Data structures (Dictionaries), Loop control.

Steps to Install & Run the Project:

Prerequisites: 
Make sure you have **Python 3** installed on your machine. You can check by running:
```bash
python --version
```

Installation: 
1. Clone or Download the project repository to your local machine.
2. Ensure your project directory has the following structure:
    ```
   smartbudget/
   ├── get_income.py
   ├── get_expenses.py
   └── main.py
   ```

Running the Application: 
Open your terminal or command prompt, navigate to the project directory, and execute the main file:
```bash
python main.py
```

---

Instructions for Testing:

To verify that the application handles errors and calculations correctly, test the following scenarios:

1. Valid Run (Saving Money):
   * Income: `5000`
   * Expenses: `food: 200`, `rent: 1500`, type `done`.
   * *Expected Output:* `Good job! You have saved: 3300.00`

2. Over-budget Alert:
   * Income: `1000`
   * Expenses: `rent: 1200`, type `done`.
   * *Expected Output:* `WARNING: You have exceeded your budget. Try cutting back on essentials.`

3. Input Validation (Robustness):
   * When asked for income, type `hello`. The application should catch the error and ask you to enter a valid value again.
   * When asked for an expense amount, type `abc`. It should display `Please enter valid input` and let you retry the amount.

---

 Screenshots:

Application Walkthrough: 
<img width="533" height="421" alt="Screenshot 2026-09-28 225455 bob" src="https://github.com/user-attachments/assets/952128f5-b3e3-44de-b5c6-9b91bdf66c22" />


