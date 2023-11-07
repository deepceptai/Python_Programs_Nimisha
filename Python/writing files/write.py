# write is used to override the file
employee_file = open("emp.txt", "w")
employee_file.write("\nKelly - Customer Service ")
employee_file.close()

# write is used to write txt in a new file
employee_file = open("emp1.txt", "w")
employee_file.write("\nToby - Human resources")
employee_file.close()

# write can also be used to write a html file
employee_file = open("index.html", "w")
employee_file.write("<p>This is html</p>")
employee_file.close()
