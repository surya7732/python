# Question: Electricity Bill Calculator
# Write a Python program to calculate the electricity bill based on the following tariff:

# For the first 100 units: ₹1.50 per unit
# For the next 100 units (101-200): ₹2.50 per unit
# Beyond 200 units: ₹3.50 per unit
# Additionally:

# Add a fixed service charge of ₹50 to the total bill.
# If the input is invalid (negative units), display "Invalid input!".
units=int(input("Enter the units consumed:"))
service_charge=50
bill=0
if units<0:
    print("input is invalid(negative units)! ")
else :
    if units<=100:
        bill=units*1.50
    elif units<=200:
        bill=(100*1.50)+(units-100)*2.50
    elif units>200:
         bill=(100*1.50)+(100*2.50)+(units-200)*3.50
    else:
          bill=(100*1.50)+(100*2.50)+(100*3.50)+(units-300)*5
    total_bill=bill+service_charge
    print(f"bill is:{total_bill :.2f} ")
