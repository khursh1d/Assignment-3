ssum = 0
count = 0

while True:
    try:
#Getting the input from the user
        num = input("Enter a number (or 'done' to exit): ")
        if num.lower() == "done":
            break
        num = float(num)
        sum += num
        count += 1
#Printing the error message
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")
#Functions Summ, count and Average number
if count > 0:
    average = sum / count
    print("Sum of input numbers :", sum)
    print("Number of input :", count)
    print("Average of input numbers:", average)
#Error message
else:
    print("invalid input. enter a number.")

#Name: Bakhtiyorov Khurshidbek Khamdam Ugli
#Student ID:202312403
#Class number (003)
