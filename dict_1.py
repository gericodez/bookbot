# create a dictionary with typing keyes and values - names and emails
contacts = {
    'Bob' : 'ilovebunnies@gmail.com',
    'Wendy' : 'ilovebirds@hotmail.com',
    'Cecilia' : 'ilovecats@outlook.com'
}

print(contacts)
#add a new item to the dictionary with key and value
contacts['Alex'] = "coolalex@gamemail.com"
#print  the dictionary with keys and values
print(contacts)
#remove Wendy from dictionary with pop method
contacts.pop('Wendy')
#print  the dictionary with keys and values
print(contacts)
#print keys from dictionary with keys method
print(contacts.keys()) 
#search for a name Alex (a key) in the contacts dictionary - key() method
for key in contacts.keys():
    if key == 'Alex':
        print ('Alex is in contacts')
# is ilovebunnies@gmail in the contact list? values() method
for value in contacts.values():
    if value == 'ilovebunnies@gmail.com':
        print ('ilovebunnies@gmail is in the list')
# woho's email address is 'ilovebunnies@gmail.com' ?
for key, value in contacts.items():
    if value == 'ilovebunnies@gmail.com':
        print (value, '->', key )    



# Problem 1 – Creating Your First Dictionary
#Create a dictionary named `favorite_colors` that stores the favorite colors of three friends:

favorite_colors = {
'Alice' : "blue",
'Bob' : 'green',
'Carol' : 'red'
}
print('Problem 1', favorite_colors)

# Problem 2 – Accessing Values by Keys
print('Problem 2',favorite_colors['Bob'])

#Problem 3 – Adding and Removing Entries
#- Add Eve to the `favorite_colors` dictionary.
# Then, suppose Alice moved away — remove Alice from the dictionary. pop
# Print the updated dictionary.

favorite_colors['Eve'] = 'purple'
print('Problem 3', favorite_colors)
favorite_colors.pop('Alice')
print('Problem 3', favorite_colors)

# Problem 4 – Dictionaries vs. Lists
# You have two collections of email addresses:
# As a list
emails_list = ["bob@gmail.com", "carol@gmail.com", "eve@gmail.com"]

# As a dictionary
emails_dict = {
    "Bob": "bob@gmail.com",
    "Carol": "carol@gmail.com",
    "Eve": "eve@gmail.com"
}
#Write code to get Carol’s email from the list and then from the dictionary.
#Which one feels easier, and why?
print('Problem 4', emails_list[1])
print('Problem 4', emails_dict['Carol'])

# Problem 5 – Iterating with Keys, Values, and Items
#Using the `emails_dict` above:
#- Print all the names (keys) using a loop.
#- Print all the email addresses (values) using a loop.
#- Write a loop with items() that prints messages like:
#Bob’s email is bob@gmail.com
#Carol’s email is carol@gmail.com
#Eve’s email is eve@gmail.com
print('Problem 5')
for key in  emails_dict.keys():
	print([key])
for value in  emails_dict.values():
	print([value])	
for key, value in  emails_dict.items():
	print(f"{key}'s email is {value}")	