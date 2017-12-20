# Working with files
# Your programs can read from files and write to files. Files are opened in read mode ('r') by default, but can also be
#  opened in write mode ('w') and append mode ('a').

# Reading a file and storing its lines
filename = 'siddhartha.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line)

# Writing to a file
filename = 'journal.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

# Appending to a file
filename = 'journal.txt'
with open(filename, 'a') as file_object:
    file_object.write("\nI love making games.")
