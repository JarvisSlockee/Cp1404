print("Electricity bill estimator")
cents_per_KWh = int(input("Enter cents per KWh: "))
daily_use_Kwh = float(input("Enter daily use in KWh: "))
num_billing_days = int(input("Enter number of billing days: "))
estimated_bill = (cents_per_KWh * daily_use_Kwh) * num_billing_days
print(estimated_bill)
