# Project: Employee Profile Generator (Day 3)
# Description: Practicing strings, concatenation, f-strings, and slicing.

first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name

address = '123 Main Street'
address += ', Apartment 4B'

employee_age = 28
# Using str() to convert integer to string for concatenation
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)

experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

position = 'Data Analyst'
salary = 75000
# Using f-strings for cleaner interpolation
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)

employee_code = 'DEV-2026-JD-001'

# Slicing: Extracting specific parts of the string
department = employee_code[0:3]
print(department) # DEV

year_code = employee_code[4:8]
print(year_code) # 2026

initials = employee_code[9:11]
print(initials) # JD

last_three = employee_code[-3:]
print(last_three) # 001
