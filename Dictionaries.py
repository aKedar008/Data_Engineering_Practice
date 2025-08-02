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

