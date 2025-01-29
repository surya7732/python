# Question: Leap Year Checker
# Write a Python program to check whether a given year is a leap year or not. The program should use the following rules:

# A year is a leap year if:

# It is divisible by 4, and:
# Not divisible by 100, or
# Divisible by 400.
year=int(input("Enter a year :"))
if year<0:
    print("the year cannot in the negative number")
elif (year%4==0 and year%100!=0)or(year%400==0):
    print("the given year is a leap year")
else:
    print("the given year is  not aleap year")