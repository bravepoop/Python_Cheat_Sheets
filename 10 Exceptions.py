# Exceptions
# Exceptions help you respond appropriately to errors that are likely to occur. You place code that might cause an
#  error in the try block. Code that should run in response to
#  an error goes in the except block. Code that should run only
#  if the try block was successful goes in the else block.

# Catching an exception
prompt = "How many tickets do you need? "
num_tickets = input(prompt)
try:
    num_tickets = int(num_tickets)
except ValueError:
    print("Please try again.")
else:
    print("Your tickets are printing.")
