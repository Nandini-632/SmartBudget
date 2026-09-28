# SmartBudget
Personal Finance Tracker API:
A lightweight database schema and API structure designed to map, track, and analyze personal income against corresponding expenses.

📝Overview of the Project:
This project provides a backend database structure and foundational API logic for a personal finance management tool. It uses a relational database design to create a direct link between income sources and individual expenditures.
By implementing a 1-to-many relationship between income entries and expense entries, the system allows users to allocate specific portions of their earnings directly to categorical expenses (e.g., tracking exactly which payout covered a utility bill or grocery run).

⚡Features:
• Income Logging: Track multiple streams of income with unique identifiers and precise monetary amounts.
• Categorized Expense Management: Log individual expenses, assign them to distinct operational categories, and track specific transaction  amounts.
• Relational Mapping: Bind multiple expenses to a single parent income record to monitor budget allocation dynamics.
• Data Integrity: Enforces strict relational boundaries using primary keys (PK) and foreign key relationships to prevent orphaned records.

🛠️Technologies/Tools Used:
• Database: PostgreSQL / SQLite (Relational SQL Engine)
• Design Syntax: Crow's Foot Notation / ERD ASCII standard
• Environment: Node.js / Python (Select your preferred runtime environment during setup)

⚙️Steps to Install & Run the Project:
Clone the Repository:
gh repo clone Nandini-632/SmartBudget
