print("Select operations")
print("1.Addition")
print("2.Subtraction")
print("3.Multipliccation")
print("4.Division")
operation=input("Enter any choice ")
num1=int(input("Enter a number :"))
num2=int(input("Enter a another number :"))
if operation=='1':
    result=num1+num2
    print(f"Addition of two number:{result}")
elif operation=='2':
    result=num1-num2
    print(f"Subtraction of two numbers:{result}")
elif operation=='3':
    result=num1*num2
    print(f"Multiplication of two numbers:{result}")
elif operation=='4':
     if num2!=0:
      result=num1/num2
      print(f"Division of two numbers:{result}")
     else:
      print("Error!")
else:
    print("invalid input")