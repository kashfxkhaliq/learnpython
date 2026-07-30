
monthly_income = float(input("Enter The Monthly Income :: "))
electric_bill = float(input("Enter The Electric Bill ::  "))
gas_bil = float(input("Enter The Gas Bill ::  "))
food_expenses = float(input("Enter The Food Expenses ::  "))

monthly_expenses = electric_bill + gas_bil + food_expenses
yearly_expenses = monthly_expenses * 12
monthly_saving = monthly_income - monthly_expenses
yearly_saving =  monthly_saving * 12

print("Total Monthly Expenses = ", monthly_expenses)
print("Total Yearly Expenses = ", yearly_expenses)
print("Total Monthly Saving = ", monthly_saving)
print("Total Yearly Saving = ", yearly_saving)

