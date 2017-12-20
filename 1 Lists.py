# Lists
# A list stores a series of items in a particular order. You access items using an index, or within a loop.

# Make a list
bikes = ['trek', 'redline', 'giant']

# Get the first item in a list
first_bike = bikes[0]

# Get the last item in a list
last_bike = bikes[-1]

# Looping through a list
for bike in bikes:
    print(bike)

# Adding items to a list
bikes = []
bikes.append('trek')
bikes.append('redline')
bikes.append('giant')

# Making numerical lists
squares = []
for x in range(1, 11):
    squares.append(x**2)

# List comprehensions
squares = [x**2 for x in range(1, 11)]

# Slicing a list
finishers = ['sam', 'bob', 'ada', 'bea']
first_two = finishers[:2]

# Copying a list
copy_of_bikes = bikes[:]

