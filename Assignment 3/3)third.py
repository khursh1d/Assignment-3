sum_of_numbers = 0
count = 0

while True:
    number = input("Enter a number (or 'done' to exit): ")

    if number == "done":
        break

    try:
        number = int(number)
        sum_of_numbers += number
        count += 1
    except ValueError:
        print("Invalid input. Please enter a valid number.")

#Name: Bakhtiyorov Khurshidbek Khamdam Ugli
#Student ID:202312403
#Class number (003)