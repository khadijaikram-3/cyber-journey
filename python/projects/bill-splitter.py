# Project: Bill Splitter (Day 6)
# Description: Practicing integers, floats, augmented assignment, and rounding.

running_total = 0
num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

# Augmented assignment: adding all items to the running total
running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

# Calculating the tip (25%)
tip = running_total * 0.25
print('Tip amount:', tip)

running_total += tip
print('Total with tip:', running_total)

# Dividing the bill among friends
final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

# Rounding to 2 decimal places
each_pays = round(final_bill, 2)
print(f"Each person pays: {each_pays}")
