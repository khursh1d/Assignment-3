#Getting the input from the user
try:
    hours = int(input("Enter the number of hours worked: "))
    rate = float(input("Enter the rate per hour: "))
#The programm that was asked in the ppt
    if hours > 40:
        salary = hours * rate * 1.5
    else:
        salary = hours * rate
#Printing the result
    print("Salary:", salary)
#Printing the error
except ValueError:
    print("Invalid number. Please enter a numeric value for hours.")