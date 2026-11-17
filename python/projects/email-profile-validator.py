# Project: Email Profile Validator (Day 4)
# Description: Practicing string methods, slicing, and the 'in' operator.

email = 'alice.johnson@company.com'
print(f'Email: {email}')

# Find the position of the @ symbol
at_position = email.find('@')
print(f'Position of @: {at_position}')

# Slice the string to get the username
username = email[:at_position]
print(f'Username: {username}')

# Check if specific characters exist in the string
has_at = '@' in email
print(f'Has @ symbol: {has_at}')

has_com = '.com' in email
print(f'Has .com: {has_com}')

# Cleaning up messy data
messy_name = '  sARaH dAVis  '
print(f"Original name: '{messy_name}'")

# .strip() removes whitespace, .title() capitalizes the first letter of each word
clean_name = messy_name.strip().title()
print(f"Cleaned name: '{clean_name}'")

messy_email = '  SARAH.DAVIS@COMPANY.COM  '
# .strip() removes whitespace, .lower() converts to lowercase
clean_email = messy_email.strip().lower()
print(f"Original email: '{messy_email}'")
print(f"Cleaned email: '{clean_email}'")
