def get_expenses():
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
    return expenses
    