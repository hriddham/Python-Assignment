age = int(input("Enter your age: "))
monthly_income = float(input("Enter your monthly income (in Rs): "))
credit_score = int(input("Enter your credit score: "))

valid_age = (21 <= age <= 60)

if valid_age and (monthly_income >= 30000) and (credit_score >= 700):
    print("Eligible")

elif valid_age and ((monthly_income >= 30000) or (credit_score >= 700)):
    print("Conditionally Eligible")

else:
    print("Not Eligible")