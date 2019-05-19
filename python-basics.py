import math

TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100

# Create the calvulate_price function
def calculate_price(number_of_tickets):
  return(number_of_tickets * TICKET_PRICE) + SERVICE CHARGE

# Run this code continuously until no more tickets are available
while tickets_remaining >= 1:

  # Output how many tickets are remaining using the tickets_remaining variable

  print("There are",tickets_remaining," tickets available for purchase.")

  # Gather the user's name and assign it to a new variable

  user_name = input("What is your name?   ")

  # Prompt the user by name and ask how many tickets they would like

  number_of_tickets = input("Hello, " + user_name + ". How many tickets would you like to purchase?   ")
  try:
    number_of_tickets = int(number_of_tickets)
    # Raise a ValueError if the request is for more tickets than are available
    if number_of_tickets > tickets_remaining:
       raise ValueError("There are only {} tickets remaining.".format(tickets_remaining))
  except ValueError as err:
    print("Oh no, that's not a valid input. Please try again!")

  else:
    # Calculate the price (number of tickets they want mutiplied by the price)

    total_price = TICKET_PRICE * number_of_tickets

    # Output the price to the screen
    print("The total due is ${}.".format(total_price))

    # Prompt user if they want to continue Y/N?

    continue_order = input('Would you like to continue with this order? Please type Y/N.   ')

    # If they want to proceed
    if continue_order.lower() == "y":
        # print out to the screen "SOLD!" to confirm purchase
        print("SOLD!")
        # and then decrement the tickets remaining by the number of tickets purchased
        tickets_remaining -= number_of_tickets
    #Otherwise... thank them by name
    else:
        print("Thank you anyway, {}!".format(user_name))

# Notify user that there are no more tickets available
print("Sorry. There are no more tickets available for sale.")
