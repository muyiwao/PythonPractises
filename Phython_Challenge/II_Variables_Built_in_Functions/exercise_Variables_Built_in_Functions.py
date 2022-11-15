# Exercises: Level 1

# 1 The current file
# 2 Day 2:30 Days of Python programming
# 3 Declare a first name variable and assign a value to it
first_name = 'Muyiwa'
# 4 Declare a last name variable and assign a value to it
last_name = 'Oladimeji '
# 5 Declare a full name variable and assign a value to it
full_name = 'Muyiwa Oladimeji '
# 6 Declare a country variable and assign a value to it
country = 'United Kingdom'
# 7 Declare a city variable and assign a value to it
city = 'London'
# 8 Declare an age variable and assign a value to it
age = 250
# 9 Declare a year variable and assign a value to it
year = 2022
# 10 Declare a variable is_married and assign a value to it
is_married = True
# 11 Declare a variable is_true and assign a value to it
is_true = False
# 12 Declare a variable is_light_on and assign a value to it
is_light_on = True
# 12 Declare multiple variable on one line
a, b, c = 4, "George", True



# Exercises: Level 2

# 1 Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print((type(is_true)))
print(type(is_light_on))
print(type(a))
print(type(b))
print(type(c))

# 2 Using the len() built-in function, find the length of your first name
print(len(first_name))

# 3 Compare the length of your first name and your last name
print(max(len(first_name), len(last_name)))
print(min(len(first_name), len(last_name)))

# 4 Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
# 4i Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
# 4ii Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
# 4iii Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
# 4iv Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
# 4v Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
# 4vi Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
# 4vii Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

# 5 The radius of a circle is 30 meters.
radius = 30
# 5i    Calculate the area of a circle and assign the value to a variable name of area_of_circle
pi = 3.142
area_of_circle = pi * radius ** 2
print("Area of the circle of radius %i is %f" % (radius, area_of_circle))
# 5ii   Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circumference_of_circle = 2 * pi * radius
print("Circumference of the circle of radius %i is %f" % (radius, circumference_of_circle))
# 5iii  Take radius as user input and calculate the area.
radius_2 = int(input("Enter the radius of the circle: "))
area_of_circle_2 = pi * radius_2 ** 2
print("Area of the circle of radius %i is %f" % (radius_2, area_of_circle_2))

# 6 Use the built-in input function to get first name, last name, country and age from a user and store the value to
# their corresponding variable names
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))

# 7 Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')



"""
Output
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'str'>
<class 'int'>
<class 'int'>
<class 'bool'>
<class 'bool'>
<class 'bool'>
<class 'int'>
<class 'str'>
<class 'bool'>
6
10
6
Area of the circle of radius 30 is 2827.800000
Circumference of the circle of radius 30 is 188.520000
Enter the radius of the circle: 15
Area of the circle of radius 15 is 706.950000
Enter your first name: Muyiwa
Enter your last name: Oladimeji 
Enter your country: United Kingdom
Enter your age: 250

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 


Process finished with exit code 0
"""