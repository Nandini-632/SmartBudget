SmartBudget: Project Specification

🚨 Problem Statement
Managing personal finances effectively is a common challenge for many individuals. Without a simple, lightweight system to track daily financial inputs, people often lose sight of their spending habits, leading to unintentional overspending, lack of monthly savings, and financial stress. 

Existing commercial budgeting software is frequently bloated, expensive, features steep learning curves, or requires users to link sensitive bank accounts. There is a need for a minimalist, private, and straightforward tool that provides instant clarity on an individual's financial health without unnecessary complexity.

🎯 Scope of the Project
SmartBudget is a focused, command-line interface (CLI) financial assistant. 

In-Scope:
* Individual monthly budget tracking using localized manual inputs.
* Live categorization and automated mathematical summation of expense entries.
* Basic input error handling to ensure data sanitization.
* Terminal-based reporting displaying total margins and basic budget health flags.

Out-of-Scope (Future Enhancements):
* Persistent database storage (data resets when the session closes).
* Graphic User Interfaces (GUI) or mobile application wrappers.
* Multi-user account profiles or cloud synchronization.
* Direct integration with bank APIs or automated credit card statement parsing.

👥 Target Users
* Students & Young Professionals:** Individuals looking for a quick, no-fuss way to keep tabs on basic monthly costs like rent, groceries, and books.
* Privacy-Conscious Savers:** Users who prefer not to link their bank details or personal IDs to external financial applications.
* Coding Beginners:** Anyone looking for a readable, modular Python blueprint to study fundamental programming patterns (loops, dictionary updates, exception handling).

🎛️ High-Level Features
* Modular Code Structure:** The architecture divides input capturing, processing, and output rendering into separate functional components (`get_income`, `get_expenses`, `expense_summary`).
* Continuous Expense Logging:** A dynamic capture loop allowing users to input as many categories and transaction amounts as necessary in a single session.
* Dynamic Cost Aggregation:** Smart handling of duplicate inputs—if a user logs "food" twice, the application cleanly increments the existing category total rather than overriding it.
* Real-Time Threshold Warning System:** Automatically runs programmatic comparisons against user income to flag deficits (`total_spent > income`) or break-even scenarios instantly.
