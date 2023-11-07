
employee_file = open("employee.txt", "r")

for employee in employee_file.readlines():  #to read every line in form of array
    print(employee)

employee_file.close()
