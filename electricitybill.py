units=int(input("Enter the number of units consumed:"))
bill=0
if units<0:
    print("units cannot in negative.")
elif units<=100:
    bill=units*3
elif units<=300:
    bill=100*3+(units-100)*5
else:
    bill=(100*3)+(200*5)+(units-300)*8
print(f"the electricity u consumed is:{bill}")