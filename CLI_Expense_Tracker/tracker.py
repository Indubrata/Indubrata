from datetime import datetime as dt
import os


def add_expense():
    date = input("Enter the date of the expense (DD/MM/YYYY): ")
    amount = float(input("Enter the amount of the expense: "))
    category = input("Enter the category of the expense: ")
    with open("expenses.csv", "a") as f:
        f.write(f"{date},{amount},{category}\n")
    cat.append(category)
    am.append(amount)
    dates.append(date)
    print("Expense added successfully!")

def view_expenses():
    if len(cat) == 0:
        print("No expenses added yet.")
        return
    print("How do you want to view the expenses?")
    print("1. Category-wise")
    print("2. Date-wise")
    print("3. Amount-wise")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        unique_cats = sorted(set(cat))
        for category in unique_cats:
            cat_spent = 0
            with open("expenses.csv", "r") as f:
                for line in f:
                    l = line.rstrip().split(",")
                    if category == l[2]:
                        print(f"{category}\t{l[1]}\t{l[0]}")
                        cat_spent += float(l[1])
            print(f"\nTotal amount spent in category {category} = Rs.{cat_spent}/-\n")
        print(f"\nTotal amount spent = Rs.{sum(am)}/-")
    elif choice == 2:
        global dates, dates_obj
        month_sum = 0
        date_format = "%d/%m/%Y"
        for date in dates:
            date_obj = dt.strptime(date, date_format)
            dates_obj.append(date_obj)
        dates_obj.sort(reverse=True)
        dates = []
        for date_obj in dates_obj:
            date_str = dt.strftime(date_obj, date_format)
            dates.append(date_str)
        for i in range(1, len(dates) + 1):
            with open("expenses.csv", "r") as f:
                for line in f:
                    l = line.rstrip().split(",")
                    if dates[i - 1] == l[0]:
                        print(f"{l[0]}\t{l[1]}\t{l[2]}")
                        month_sum += float(l[1])
            if (i != len(dates) and dates[i - 1].split('/')[1] != dates[i].split('/')[1]) or i == len(dates): 
                print(f"\nTotal amount spent in month {dates[i - 1].split('/')[1]} = Rs.{month_sum}/- \n")
                month_sum = 0
        dates_obj = []
    elif choice == 3:
        am.sort()
        for amount in am:
            with open("expenses.csv", "r") as f:
                for line in f:
                    l = line.rstrip().split(",")
                    if amount == float(l[1]):
                        print(f"{amount}\t{l[2]}\t{l[0]}")
    else:
        print("Please enter a valid choice and Try Again.")

def delete_expense():
    found = False
    date = input("Enter the date of the expense (DD/MM/YYYY): ")
    amount = float(input("Enter the amount of the expense: "))
    category = input("Enter the category of the expense: ")
    with open("expenses.csv", "r") as f, open("expenses_edited.csv", "w") as f2:
        for line in f:
            l = line.rstrip().split(",")
            if date != l[0] or amount != float(l[1]) or category != l[2]:
                f2.write(f"{l[0]},{l[1]},{l[2]}\n")
            elif date == l[0] and amount == float(l[1]) and category == l[2]:    
                cat.remove(category)
                am.remove(amount)
                dates.remove(date)
                found = True
    if found == True:
        os.remove("expenses.csv")
        os.rename("expenses_edited.csv", "expenses.csv")
        print("Expense deleted successfully!")
    else:
        print("Expense not found.")
                
def load_expenses():
    if os.path.exists("expenses.csv"):
        with open("expenses.csv", "r") as f:
            for line in f:
                l = line.rstrip().split(",")
                if len(l) == 3:
                    dates.append(l[0])
                    am.append(float(l[1]))
                    cat.append(l[2])
    else:
        print("No expenses found")

def update_expense():
    found = False
    date = input("Enter the date of the expense (DD/MM/YYYY): ")
    amount = float(input("Enter the amount of the expense: "))
    category = input("Enter the category of the expense: ")
    new_amount = float(input("Enter the new amount of the expense: "))
    new_category = input("Enter the new category of the expense: ")
    new_date = input("Enter the new date of the expense (DD/MM/YYYY): ")
    with open("expenses.csv", "r") as f, open("expenses_edited.csv", "w") as f2:
        for line in f:
            l = line.rstrip().split(",")
            if date != l[0] or amount != float(l[1]) or category != l[2]:
                f2.write(f"{l[0]},{l[1]},{l[2]}\n")
            elif date == l[0] and amount == float(l[1]) and category == l[2]:   
                f2.write(f"{new_date},{new_amount},{new_category}\n") 
                cat.remove(category)
                am.remove(amount)
                dates.remove(date)
                cat.append(new_category)
                am.append(new_amount)
                dates.append(new_date)
                found = True
    if found == True:
        os.remove("expenses.csv")
        os.rename("expenses_edited.csv", "expenses.csv")
        print("Expense updated successfully!")
    else:
        print("Expense not found.")


print("\tMenu")
print("1. Add Expense")
print("2. View Expenses")
print("3. Delete Expense")
print("4. Update Expense")
print("5. Exit")
print("------------------------------------------------")

cat = []
am = []
dates = []
dates_obj = []
load_expenses()
while(True):
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        delete_expense()
    elif choice == 4:
        update_expense()
    elif choice == 5:
        print("Exiting the application...Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")