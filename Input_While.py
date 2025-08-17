message = input("Tell me something, and i will repeat it back to you:")
print(message)


prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")

 

number = input("Enter a number and i'll tell you if its even or odd" )
number = int(number)

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Intro To While Loops 

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me someting, and I will repeat it back to you :"
prompt += "\nEnter 'Quit' to end the program."

active = True

message = ""
while active: 
    message = input(prompt)
    if message =="Quit":
        active = False
    else:
        print(message)

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd Love to visit {city.title()}")


current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.

prompt = "Enter the Toppings, after you are done please Enter Quit"

while True:
    pizza = input(prompt)

    if pizza == 'quit':
        break
    else:
        print(f"adding {pizza} to your pizza")


# A for loop is effective for looping through a list, but you shouldn’t modify
# a list inside a for loop because Python will have trouble keeping track of the
# items in the list. To modify a list as you work through it, use a while loop.
# Using while loops with lists and dictionaries allows you to collect, store, and
# organize lots of input to examine and report on later.     

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe Following users have been confirmed:")
for confirmed_user in confirmed_users :
    print(confirmed_user.title())

# Filling a dictionary with user input 

responses = {}

# setting a flag to indicate polling is active 
polling_activity = True

while polling_activity:
    # taking peoples name as input 
    name = input("\nWhat is your Name?")
    response = input("Which city would you like to visit")

    # storing the response in a dictionary 
    responses[name] = response

    # to check if any one else is going to take the poll
    repeat = input("Would you like to let another user take the poll (Yes/No)")
    if repeat == 'no':
        polling_activity = False

print("\n-----Poll Results-----")
for name, response in responses.items():
    print(f"{name} would like to visit {response}.")




sandwich_orders = ['cheese sandwich','pastrami','grilled sandwitch','cheese grilled sandwitch','pastrami','vegetable sandwitch','pastrami']
finished_Sandwich = []

while sandwich_orders:
    completed_order = sandwich_orders.pop()
    print(f"{completed_order} To be Prepared")

    finished_Sandwich.append(completed_order)

for i in finished_Sandwich:
    print(f"{i} is prepared, please collect it, Thank You")



sandwich_orders = ['cheese sandwich','pastrami','grilled sandwitch','cheese grilled sandwitch','pastrami','vegetable sandwitch','pastrami']


finished_Sandwich = []

print("The deli has run out of pastrami.")

# Remove all occurrences of 'pastrami'
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    completed_order = sandwich_orders.pop()
    print(f"{completed_order} To be Prepared")

    finished_Sandwich.append(completed_order)

for i in finished_Sandwich:
    print(f"{i} is prepared, please collect it, Thank You")
