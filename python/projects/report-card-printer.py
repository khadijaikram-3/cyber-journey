# Project: Report Card Printer
# Date: Day 1 (Nov 11, 2026)
# Description: Practicing variables, data types, and the type() / isinstance() functions.

# 1. String (str)
name = 'Alice'
print(name, type(name)) 
# Output: Alice <class 'str'>

# 2. Boolean (bool)
is_student = True
print(is_student, type(is_student))
# Output: True <class 'bool'>

# 3. Integer (int)
age = 20
print(age, type(age))
# Output: 20 <class 'int'>

# 4. Float (float)
score = 80.5
print(score, type(score))
# Output: 80.5 <class 'float'>

# 5. Checking types with isinstance()
# This checks if 'score' is a float. Since it is, it prints True.
print(isinstance(score, float))
# Output: True
