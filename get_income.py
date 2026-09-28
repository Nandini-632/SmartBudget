def get_income():
    try:
        income=float(input("Enter your total monthly income: "))
        return income
    except ValueError:
        print("Please enter a numerical value")
        return