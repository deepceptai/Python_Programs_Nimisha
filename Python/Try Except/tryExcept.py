try:
    value = 10/0
except ZeroDivisionError as err:
    print(err)


try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")

