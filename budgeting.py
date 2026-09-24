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
  #Adding gui  
def run_gui():
    """Launches the graphical version of SmartBudget."""
    #Variables
    state = {
        "income": 0.0,
        "expenses": {}
    }
    
    def set_income():
        try:
            val = float(income_entry.get())
            if val < 0:
                raise ValueError
            state["income"] = val
            add_expense_btn.config(state=tk.NORMAL)
            update_summary()
            income_entry.config(state=tk.DISABLED)
            set_income_btn.config(state=tk.DISABLED)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid, positive numerical value for income.")

    def add_expense():
        category = category_entry.get().strip().capitalize()
        amount_str = amount_entry.get().strip()
        
        if not category:
            messagebox.showerror("Missing Field", "Please enter an expense category.")
            return
            
        try:
            amount = float(amount_str)
            if amount <= 0:
                raise ValueError
                
            if category in state["expenses"]:
                state["expenses"][category] += amount
            else:
                state["expenses"][category] = amount
                
            category_entry.delete(0, tk.END)
            amount_entry.delete(0, tk.END)
            update_summary()
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number greater than zero for the amount.")

    def update_summary():
        total_spent = sum(state["expenses"].values())
        remaining = state["income"] - total_spent
        
        lbl_income.config(text=f"Total Income: {state['income']:.2f}")
        lbl_spent.config(text=f"Total Spent: {total_spent:.2f}")
        lbl_remaining.config(text=f"Remaining Cash: {remaining:.2f}")
        
        expense_listbox.delete(0, tk.END)
        for cat, amt in state["expenses"].items():
            expense_listbox.insert(tk.END, f" {cat:<18} : {amt:>9.2f}")
            
        if total_spent > state["income"]:
            lbl_status.config(text="⚠️ WARNING: You have exceeded your budget! Try cutting back on essentials.", foreground="#d9534f")
            lbl_remaining.config(foreground="#d9534f")
        elif remaining == 0:
            lbl_status.config(text="ℹ️ You have spent your entire budget. Try saving next time.", foreground="#f0ad4e")
            lbl_remaining.config(foreground="#f0ad4e")
        else:
            lbl_status.config(text=f"✅ Good job! You have safely saved {remaining:.2f} so far.", foreground="#5cb85c")
            lbl_remaining.config(foreground="#5cb85c")

    # GUI Window Setup
    root = tk.Tk()
    root.title("SmartBudget - Personal Finance Tracker")
    root.geometry("650x450")
    root.resizable(False, False)
    
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TLabel", font=("Segoe UI", 10))
    style.configure("TButton", font=("Segoe UI", 10), padding=5)
    style.configure("Header.TLabel", font=("Segoe UI", 12, "bold"))
    
    main_frame = ttk.Frame(root, padding=20)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    left_frame = ttk.Frame(main_frame, width=280)
    left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
    
    right_frame = ttk.Frame(main_frame, width=320)
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
    
    # Left Panel Layout
    ttk.Label(left_frame, text="Income & Expenses", style="Header.TLabel").pack(anchor=tk.W, pady=(0, 15))
    ttk.Label(left_frame, text="Monthly Income:").pack(anchor=tk.W)
    income_entry = ttk.Entry(left_frame, font=("Segoe UI", 10))
    income_entry.pack(fill=tk.X, pady=(0, 10))
    
    set_income_btn = ttk.Button(left_frame, text="Set Income", command=set_income)
    set_income_btn.pack(fill=tk.X, pady=(0, 20))
    
    ttk.Label(left_frame, text="Expense Category (e.g., Food, Rent):").pack(anchor=tk.W)
    category_entry = ttk.Entry(left_frame, font=("Segoe UI", 10))
    category_entry.pack(fill=tk.X, pady=(0, 10))
    
    ttk.Label(left_frame, text="Amount:").pack(anchor=tk.W)
    amount_entry = ttk.Entry(left_frame, font=("Segoe UI", 10))
    amount_entry.pack(fill=tk.X, pady=(0, 10))
    
    add_expense_btn = ttk.Button(left_frame, text="Add Expense", command=add_expense, state=tk.DISABLED)
    add_expense_btn.pack(fill=tk.X, pady=(0, 5))
    
    # Right Panel Layout
    ttk.Label(right_frame, text="Budget Summary", style="Header.TLabel").pack(anchor=tk.W, pady=(0, 15))
    
    metrics_box = ttk.LabelFrame(right_frame, padding=10)
    metrics_box.pack(fill=tk.X, pady=(0, 15))
    
    lbl_income = ttk.Label(metrics_box, text="Total Income: 0.00", font=("Segoe UI", 10, "bold"))
    lbl_income.pack(anchor=tk.W, pady=2)
    
    lbl_spent = ttk.Label(metrics_box, text="Total Spent: 0.00", font=("Segoe UI", 10, "bold"), foreground="#d9534f")
    lbl_spent.pack(anchor=tk.W, pady=2)
    
    lbl_remaining = ttk.Label(metrics_box, text="Remaining Cash: 0.00", font=("Segoe UI", 10, "bold"), foreground="#5cb85c")
    lbl_remaining.pack(anchor=tk.W, pady=2)
    
    lbl_status = ttk.Label(right_frame, text="Please enter your monthly income to begin.", wraplength=300, justify=tk.LEFT)
    lbl_status.pack(fill=tk.X, pady=(0, 15))
    
    ttk.Label(right_frame, text="Expense Log:").pack(anchor=tk.W)
    expense_listbox = tk.Listbox(right_frame, font=("Consolas", 10), height=8)
    expense_listbox.pack(fill=tk.BOTH, expand=True)
    
    root.mainloop()

# 3. CONTROLLER SWITCH

if __name__ == "__main__":
    # Change 'run_gui()' to 'main()' if you want to run the terminal text tracker instead.
    run_gui()
