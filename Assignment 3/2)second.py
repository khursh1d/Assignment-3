#Getting input from the users
score = int(input("Enter the score (between 0 and 100): "))
#The function seperates the result
if score < 0 or score > 100:
    print("Error: Score is out of range.")
else:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
#Printing the result
    print("Grade:", grade)