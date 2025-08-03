#Dictionaries practice
# A dictionary in Python is a collection of key-value pairs

alien_0 = {'color': 'green', 'points':5}

print(alien_0['color'])
print(alien_0['points'])

#after defeting alein_0 
new_points = alien_0['points']
print(f"You just scored {new_points} points")

# Adding new-Key value pairs 
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

#let's track the movement/position of an alien that can move at diff speed 
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
 x_increment = 1
elif alien_0['speed'] == 'medium':
 x_increment = 2
else:
 # This must be a fast alien.
 x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

# removing key value pairs
alien_0 = {'color': 'green', 'points':5}
del alien_0['points']
print(alien_0)

# You can also use a dictionary to store one kind of information about many objects

favorite_language = {
    'Jen' : 'Pyhton',
    'Sarah' : 'C',
    'Edward': 'Ruby',
    'Phil': 'Pyhton'
}
language = favorite_language['Sarah'].title()
print(f"Sarah's favorite language is {language}")

# Using get() to Access Values

point_value = alien_0.get('points','No point value assigned')
print(point_value)

# TIY 6.1 Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.

person = {
    'f_name': 'Shlok',
    'l_name': 'Kedar',
    'Age': 19,
    'City': 'Nagpur',    
}

print(f"First Name: {person['f_name']}")
print(f"Last Name: {person['l_name']}")
print(f"Age: {person['Age']}")
print(f"City: {person['City']}")

# Looping through the Dictionary 
# Looping Through All Key-Value Pairs

user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value:{value}")

for name, language in favorite_language.items():
    print(f"{name.title()}'s favurite language is {language.title()}.")

# just looping through the key's

for name in favorite_language.keys():
    print(name.title())

friends = ['Phil','Sarah']
for name in favorite_language.keys():
    print(name.title())

    if name in friends:
        language = favorite_language[name].title()
        print(f"\t{name.title()},I see you love {language}!")

# Using sorted function with dictionary

for name in sorted(favorite_language.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Now Looping through all the values

print("The following languages have been mentioned:")
# for language in favorite_language.values():
#     print(language.title())

# A set is a collection in which each item must be unique:

for language in set(favorite_language.values()):
    print(language.title())

# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# •	 Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# •	 Use a loop to print the name of each river included in the dictionary.
# •	 Use a loop to print the name of each country included in the dictionary.

rivers = {'nile':'egypt','ganga':'india','amazon':'brazil'}

for key,value in rivers.items():
    print(f"The {key.title()} runs through {value.title()}")

for key in rivers.keys():
    print(key.title())

for value in rivers.values():
    print(value.title())

# Sometimes you’ll want to store multiple dictionaries in a list, or a list of
# items as a value in a dictionary. This is called nesting. You can nest dictionaries inside a list, a list of items inside a dictionary, or even a dictionary inside
# another dictionary.

# In the following example we
# use range() to create a fleet of 30 aliens:
#make empty list for storing aliens
aliens =  []
#creating 30 aliens
for alien_number in range (30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")

print(f"Total number of aliens : {len(aliens)}")

# # , to change the
# first three aliens to yellow, mediumspeed aliens worth 10 points each, we
# could do this:

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens[:5]:
    print(alien)
print("...")

# Store information about a pizza being ordered.
pizza = {
   'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
 }
# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell']
}
for name, languages in favorite_languages.items():
    if len(languages) < 2 :
        print(f"\n{name.title()}'s favorite language is:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")

# A Dictionary in a Dictionary

users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
    },
    'mcurie':{
        'first':'maire',
        'last':'curie',
        'location':'pairs'
    }
}

for username,user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")