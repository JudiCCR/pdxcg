#filename: lab03_grading.py

#random module imported for rival test
import random

#filename: grading.py
#user prompt
grade1=input("Enter grade between 0 and 100: ")
print(f"You entered a score of ", grade1)


#function to determine if input is a valid
def isFloat(grade):
    try:
        grade = float(grade)
        if grade in range(0,100):
            return True
    except ValueError:
        return False
#protection from improper input
if isFloat(grade1):
    grade1 = float(grade1)
    yga=("Your letter grade is: ")

    #rival grade
    grade2=random.uniform(0,100)

    #sorting instructions
    if 89<grade1<=100:
        print(yga, "A")

    elif 79<grade1<89:
        print(yga, "B")

    elif 69<grade1<79:
        print(yga, "C")

    elif 59<grade1<69:
        print(yga, "D")

    elif grade1<=59:
        print(yga, "F")

    print("Your rival's score was", grade2)

    if grade1>grade2:
        print("You did better than your rival!")

    else:
        print("Your rival has beaten you :(")

else:
    print("Please enter a valid input")
