# Question: Grade Calculator
# Write a Python program that takes a student's marks as input for five subjects. The program should calculate the total marks, percentage, and grade based on the following criteria:

# Grade A: Percentage ≥ 90
# Grade B: 80 ≤ Percentage < 90
# Grade C: 70 ≤ Percentage < 80
# Grade D: 60 ≤ Percentage < 70
# Grade F: Percentage < 60
sub1=int(input("Enter DAA marks:"))
sub2=int(input("Enter IDE marks:"))
sub3=int(input("Enter DPPM marks:"))
sub4=int(input("Enter STM marks:"))
sub5=int(input("Enter CD marks:"))
if (0<=sub1<=100)and(0<=sub2<=100)and(0<=sub3<=100)and(0<=sub4<=100)and(0<=sub5<=100):
    total_marks=sub1+sub2+sub3+sub4+sub5
    percentage=(total_marks/500)*100
    if percentage>=90:
        print("you got Grade A")
    elif percentage>=80:
        print("you got Grade B")
    elif percentage>=70:
        print("you got Grade C")
    elif percentage>=60:
        print("you got Grade D")
    else:
        print("you got Grade F")
    print(f"total marks :{total_marks}")
    print(f"percentage:{percentage}")
else:
    print("Invalid! The marks cannot in negative")