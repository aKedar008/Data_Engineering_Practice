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