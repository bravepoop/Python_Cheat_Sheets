# If Statements
# If statements are used to test for particular conditions and respond appropriately.

# Conditional tests
x = 4

# equals
if x == 42:
    print('this')
# not equal
if x != 42:
    print('this')
# greater than
if x > 42:
    print('this')
# greater than or equal to
if x >= 42:
    print('this')
# less than
if x < 42:
    print('this')
# less than or equal to
if x <= 42:
    print('this')

# Conditional test with lists
bikes = ['trek', 'redline', 'giant']

'trek' in bikes
'surly' not in bikes

# Assigning boolean values
game_active = True
can_edit = False

# A simple if test
age = x

if age >= 18:
    print("You can vote!")

# If-elif-else statements
if age < 4:
    ticket_price = 0
elif age < 18:
    ticket_price = 10
else:
    ticket_price = 15
