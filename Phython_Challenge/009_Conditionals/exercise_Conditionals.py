# Exercises: Day 9
# Exercises: Level 1
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback:
# You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print("You need %i more years to learn to drive." % (18 - age))
"""
Output:
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive."""

# 2  Compare the values of my_age and your_age using if … else.
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
# You can use a nested condition to print 'year' for 1 year difference in age,
# 'years' for bigger differences, and a custom text if my_age = your_age.

my_age = int(input("Enter age: "))
your_age = int(input("Enter your age: "))

age_gap = your_age - age
if your_age > my_age:
    if age_gap == 1:
        print("You are %i year older than me" % age_gap)
    else:
        print("You are %i years older than me" % age_gap)
elif your_age == my_age:
    print("We are the same age")
else:
    if age_gap == -1:
        print("I am %i year older than you" % abs(age_gap))
    else:
        print("I am %i year older than you" % abs(age_gap))

"""
# Output:
Enter your age: 30
You are 5 years older than me."""

# Get two numbers from the user using input prompt.
# If a is greater than b return a is greater than b,
# if a is less b return a is smaller than b, else a is equal to b.

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print("%i is greater than %i" % (a, b))
elif a < b:
    print("%i is smaller than %i" % (a, b))
else:
    print("%i is equal to %i" % (a, b))

"""Output:
Enter number one: 4
Enter number two: 3
4 is greater than 3"""

# Exercises: Level 2
# 1. Write a code which gives grade to students according to theirs scores:

score = int(input("Enter student score: "))

if 80 <= score <= 100:
    print("A")
elif 70 <= score <= 89:
    print("B")
elif 60 <= score <= 69:
    print("C")
elif 50 <= score <= 59:
    print("D")
else:
    print("F")

# 2. Check if the season is Autumn, Winter, Spring or Summer.
# If the user input is: September, October or November, the season is Autumn.
# December, January or February, the season is Winter.
# March, April or May, the season is Spring
# June, July or August, the season is Summer

month = str(input("Enter month: "))

if month in ['September', 'October', 'November']:
    print('Autumn')
elif month in ['December', 'January', 'February']:
    print('Winter')
elif month in ['March', 'April', 'May']:
    print('Spring')
else:
    print('Summer')

# 3. The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and
# print the modified list. If the fruit exists print('That fruit already exist in the list')
fruit = str(input("Enter fruit: "))

if fruit not in fruits:
    fruits.append(fruit)
    print(fruits)
else:
    print('That fruit already exist in the list')

# Exercises: Level 3
# 4. Here we have a person dictionary. Feel free to modify it!

person = {
    'first_name': 'Muyiwa',
    'last_name': 'Oladimeji',
    'age': 250,
    'country': 'United Kingdom',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in list(person.keys()):
    skills_lst = person.get('skills')
    skills_lst_len = len(skills_lst)
    print(skills_lst[skills_lst_len // 2])

# * Check if the person dictionary has skills key,
# if so check if the person has 'Python' skill and print out the result.
if 'skills' in list(person.keys()):
    skills_lst = person.get('skills')
    if 'Python' in skills_lst:
        print("The person has Python skill")
    else:
        print("No Python skill")

# * If a person skills has only JavaScript and React, print('He is a front end developer'),
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
# if the person skills has React, Node and MongoDB,Print('He is a fullstack developer'),
# else print('unknown title') -# for more accurate results more conditions can be nested!
skills_num = int(input("How many skills do you have: "))

i = 0
skill_bucket = []
while i < skills_num:
    skill = str(input("Enter skill: "))
    skill_bucket.append(skill)
    i += 1

skills_set = set(skill_bucket)
if skills_set == set(['JavaScript', 'React']):
    print('He is a front end developer')
elif skills_set == set(['Node', 'Python', 'MongoDB']):
    print('He is a backend developer')
elif skills_set == set(['React', 'Node', 'MongoDB']):
    print('He is a fullstack developer')
else:
    print('unknown title')

# * If the person is married and if he lives in United Kingdom', print the information in the following format:

if person.get('is_married') and person.get('country') == 'United Kingdom':
    print(person.get('first_name') + " " + person.get('last_name') + " lives in " +
          person.get('country') + ". He is married")
else:
    print("Invalid entry")

"""
Output:
Enter your age: 15
You need 3 more years to learn to drive.
Enter age: 15
Enter your age: 16
You are 1 year older than me
Enter number one: 4
Enter number two: 3
4 is greater than 3
Enter student score: 61
C
Enter month: February
Winter
Enter fruit: pawpaw
['banana', 'orange', 'mango', 'lemon', 'pawpaw']
Node
The person has Python skill
How many skills do you have: 3
Enter skill: React
Enter skill: MongoDB
Enter skill: Node
He is a fullstack developer
Muyiwa Oladimeji lives in United Kingdom. He is married

Process finished with exit code 0
"""
