# Write a Python program that takes three sides of a triangle as input and determines the type of triangle. The program should use the following conditions:

# Equilateral Triangle: All three sides are equal.
# Isosceles Triangle: Any two sides are equal.
# Scalene Triangle: All three sides are different.
# Check if the given sides can form a triangle:
# The sum of any two sides should be greater than the third side.
s1=int(input("Enter side1 of triangle:"))
s2=int(input("Enter side2 of triangle:"))
s3=int(input("Enter side3 of triangle:"))
if (s1+s2>s3)and(s2+s3>s1)and(s3+s1>s2):
    if (s1==s2==s3):
        print("the triangle is equilateral.")
    elif (s1!=s2!=s3):
        print("the  triangle is scalene. ")
    else:
        print("the triangle is Isosceles.")
else:
    print("the given sides cannot form a triangle")