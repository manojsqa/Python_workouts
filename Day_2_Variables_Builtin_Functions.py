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

"""
Assignments on Variables and Data Types

Exercises: Level 1

1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
2. Write a python comment saying 'Day 2: 30 Days of python programming'
3. Declare a first name variable and assign a value to it
4. Declare a last name variable and assign a value to it
5. Declare a full name variable and assign a value to it
6. Declare a country variable and assign a value to it
7. Declare a city variable and assign a value to it
8. Declare an age variable and assign a value to it
9. Declare a year variable and assign a value to it
10. Declare a variable is_married and assign a value to it
11. Declare a variable is_true and assign a value to it
12. Declare a variable is_light_on and assign a value to it
13. Declare multiple variable on one line


Exercises: Level 2
1. Check the data type of all your variables using type() built-in function
2. Using the len() built-in function, find the length of your first name
3. Compare the length of your first name and your last name
4. Declare 5 as num_one and 4 as num_two
5. Add num_one and num_two and assign the value to a variable total
6. Subtract num_two from num_one and assign the value to a variable diff
7. Multiply num_two and num_one and assign the value to a variable product
8. Divide num_one by num_two and assign the value to a variable division
9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
10. Calculate num_one to the power of num_two and assign the value to a variable exp
11. Find floor division of num_one by num_two and assign the value to a variable floor_division
12. The radius of a circle is 30 meters.
12.1. Calculate the area of a circle and assign the value to a variable name of area_of_circle
12.2. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
12.3. Take radius as user input and calculate the area.
13. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
14. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords




"""
