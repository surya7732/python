# a=int(input("Enter a number:"))
# b=int(input("Enter b number:"))
# temp=a
# a=b
# b=temp
# print(f" value of a is {a}")
# print(f" value of b is {b}")
a=int(input("Enter a number:"))
b=int(input("Enter b number:"))
# a,b=b,a
# print(f"After swaping :\n a={a} \n b={b}")
a=a+b
b=a-b
a=a-b
print(f" value of a is {a}")
print(f" value of b is {b}")