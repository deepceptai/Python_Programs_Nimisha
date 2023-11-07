# r - read (can read cannot modify) 
# w - write (can modify and add new info)
# a - append(can't modify but can add some info at end of the file)
# r+ - read and write

employee_file = open("employee.txt", "r")

print(employee_file.readable())  #to check whether the file is in read or not

#readline() --> used to read an individual line
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())

employee_file.close()    #to close the file 

