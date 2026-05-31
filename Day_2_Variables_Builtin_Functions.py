# Day_2:- Variables and Built in Functions

first_name = "Manoj"          # assignng a variable
last_Name = "Kumar"
country = "INDIA"
state = "Karnataka"
city = "Bengaluru"
skills = ["python", "Virtualisation", "RAID", "Server_Validation", "Silicon_Validation"]
age = 30
is_married = True

person_info = {'first_name': 'Manoj', 'last_name': 'Kumar', 'country': 'INDIA', 'state': 'Karnataka', 'city': 'Bengaluru'}     # a person_Information 


# printing the values stored in the variables

print('first_name: ', first_name)
print('last_name: ', last_Name)
print('length of first_name : ', len(first_name))
print('length of last name: ', len(last_Name))
print('country: ', country)
print('state: ', state)
print('city: ', city)
print('age: ', age)
print('maried: ', is_married)
print('skills: ', skills)
print('person_information: ', person_info)


# Declaring multiplae variables in a single line


first_name, last_Name, age, city, state, country, is_married = 'Manoj', 'Kumar', 30, 'Bengaluru', 'Karnataka', 'India', 'True' 

print('first name: ', first_name) 
print('length_of_first_name: ' , len(first_name))

print('last_name: ', last_Name)
print('length_of_last_name: ' , len(last_Name))
print('age: ', age)
print('city: ', city)
print('state: ', state)
print('Country: ',  country)
print('Married: ', is_married)


# geting an input from an user

first_name = str(input("enter your first name:=> "))
print('your first name: ', first_name)








