#budgetting code for students
def main():
    print("Welcome to SmartBudget!")
    try:
        income=float(input("Enter yout total monthly income: "))
    except ValueError:
        print("Please enter a numerical value")
        return
    expenses={}         #store expenses by category
    print("Please enter your expenses\n" \
    "type 'done' when finished\n")
    while True:
        category=input("Enter expenses(eg:food,rent,books etc.): ").strip()
        if category.lower()=="done":
            break
        try:
           amount=float(input("enter amount for {category}: "))
           if category in expenses:
            expenses[category]+=amount
           else:
            expenses[category]=amount
        except ValueError:
           print("Please enter valid input")
    total_spent=sum(expenses.values())      #calc. savings and expenses
    remaining=income-total_spent
    print("\n Budgeting summary:")
    print(f"Total Income:   {income:.2f}")
    print(f"Total Spent:    {total_spent:.2f}")
    print(f"Remaining Cash: {remaining:.2f}")
    if total_spent>income:
        print("WARNING: You have exceeded your budget. Try cutting back on essentials.")
    elif remaining==0:
        print("You have spent your entire budget. Try saving next time.")
    else:
        print("Good job! you have saved: ",remaining)
    
if __name__ == "__main__":
    main()
