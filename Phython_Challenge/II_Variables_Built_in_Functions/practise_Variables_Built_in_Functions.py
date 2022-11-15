# Built-in Functions
print('Hello World!')
print(len("Hello World"))
print(type("Hello World"))
print(type(str(10)))
print(type(int("10")))
print(float(10))
name = input('Enter your name: ')
print(dir(str))
print(min(30, 40, 50))
print(max(30, 40, 50))
print(sum([20, 30, 40]))

# Variables in Python
first_name = 'Muyiwa'
last_name = 'Oladimeji'
country = 'United Kingdom '
city = 'London'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {'firstname': 'Muyiwa',
               'lastname': 'Oladimeji',
               'country': 'United Kingdom ',
               'city': 'London'
               }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

first_name, last_name, country, age, is_married = 'Muyiwa', 'Oladimeji', 'London', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)

# Checking Data types and Casting

# Different python data types
# Let's declare variables with various data types

first_name = 'Muyiwa'  # str
last_name = 'Oladimeji'  # str
country = 'United Kingdom'  # str
city = 'London'  # str
age = 250  # int, it is not my real age, don't worry about it

# Printing out types
print(type('Muyiwa'))  # str
print(type(first_name))  # str
print(type(10))  # int
print(type(3.14))  # float
print(type(1 + 1j))  # complex
print(type(True))  # bool
print(type([1, 2, 3, 4]))  # list
print(type({'name': 'Muyiwa', 'age': 250, 'is_married': 250}))  # dict
print(type((1, 2)))  # tuple
print(type(zip([1, 2], [3, 4])))  # set

# int to float
num_int = 10
print('num_int', num_int)  # 10
num_float = float(num_int)
print('num_float:', num_float)  # 10.0

# float to int
gravity = 9.81
print(int(gravity))  # 9

# int to str
num_int = 10
print(num_int)  # 10
num_str = str(num_int)
print(num_str)  # '10'

# str to int or float
num_str = '10.6'
print('num_int', int(float(num_str)))  # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Muyiwa'
print(first_name)  # 'Muyiwa'
first_name_to_list = list(first_name)
print(first_name_to_list)  # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']

"""
Output:
Hello World!
11
<class 'str'>
<class 'str'>
<class 'int'>
10.0
Enter your name: Muyiwa
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
30
50
90
First name: Muyiwa
First name length: 6
Last name:  Oladimeji
Last name length:  9
Country:  United Kingdom 
City:  London
Age:  250
Married:  True
Skills:  ['HTML', 'CSS', 'JS', 'React', 'Python']
Person information:  {'firstname': 'Muyiwa', 'lastname': 'Oladimeji', 'country': 'United Kingdom ', 'city': 'London'}
Muyiwa Oladimeji London 250 True
First name: Muyiwa
Last name:  Oladimeji
Country:  London
Age:  250
Married:  True
What is your name: Muyiwa
How old are you? 250
Muyiwa
250
<class 'str'>
<class 'str'>
<class 'int'>
<class 'float'>
<class 'complex'>
<class 'bool'>
<class 'list'>
<class 'dict'>
<class 'tuple'>
<class 'zip'>
num_int 10
num_float: 10.0
9
10
10
num_int 10
num_float 10.6
Muyiwa
['M', 'u', 'y', 'i', 'w', 'a']

Process finished with exit code 0
"""
