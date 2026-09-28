#budgetting code for students
import get_income
import get_expenses
def expense_summary(income,expenses):
    total_spent=sum(expenses.values())     #calc. savings and expenses
    remaining=income-total_spent
    print(f"\n Budgeting summary:")
    print(f"Total Income:   {income:.2f}")
    print(f"Total Spent:    {total_spent:.2f}")
    print(f"Remaining Cash: {remaining:.2f}")
    if total_spent>income:
        print("WARNING: You have exceeded your budget. Try cutting back on essentials.")
    elif remaining==0:
        print("You have spent your entire budget. Try saving next time.")
    else:
        print("Good job! you have saved: ",remaining)
    return expense_summary
def main():
    print("Welcome to SmartBudget!")
    income=get_income.get_income()
    expenses=get_expenses.get_expenses()
    expense_summary(income,expenses)
if __name__ == "__main__": 
    main()
