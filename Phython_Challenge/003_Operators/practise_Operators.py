# Boolean
print(True)
print(False)

# Operators
# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 3)  # 4
print('Subtraction: ', 3 - 1)  # 2
print('Multiplication: ', 3 * 3)  # 9
print('Division: ', 4 / 4)  # 1.0  Division in Python gives floating number
print('Division: ', 6 / 4)  # 1.5
print('Division: ', 7 / 4)  # 1.75
print('Division without the remainder: ', 9 // 3)  # 3,  gives without the floating number or without the remaining
print('Division without the remainder: ', 9 // 4)  # 2
print('Modulus: ', 4 % 3)  # 1, Gives the remainder
print('Exponentiation: ', 3 ** 3)  # 27 it means 3 * 3 * 3

# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ', (1 + 1j) * (1 - 1j))

# Declaring the variable at the top first

a = 3  # a is a variable name and 3 is an integer data type
b = 2  # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
print(total)  # if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)

# Calculating area of a circle
radius = 10  # radius of a circle
area_of_circle = 3.14 * radius ** 2  # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')  # Adding unit to the weight

# Calculate the density of a liquid
mass = 75  # in Kg
volume = 0.075  # in cubic meter
density = mass / volume  # 1000 Kg/m^3

# Comparison Operators
print(3 > 2)  # True, because 3 is greater than 2
print(3 >= 2)  # True, because 3 is greater than 2
print(3 < 2)  # False,  because 3 is greater than 2
print(2 < 3)  # True, because 2 is less than 3
print(2 <= 3)  # True, because 2 is less than 3
print(3 == 2)  # False, because 3 is not equal to 2
print(3 != 2)  # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))  # True
print(len('milk') != len('meat'))  # False
print(len('milk') == len('meat'))  # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))  # False

# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('1 is 1', 1 is 1)  # True - because the data values are the same
print('1 is not 2', 1 is not 2)  # True - because 1 is not 2
print('A in Muyiwa', 'A' in 'Muyiwa')  # True - A found in the string
print('B in Muyiwa', 'B' in 'Muyiwa')  # False - there is no uppercase B
print('coding' in 'coding for all')  # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')  # True
print('4 is 2 ** 2:', 4 is 2 ** 2)  # True
print(3 > 2 and 4 > 3)  # True - because both statements are true
print(3 > 2 and 4 < 3)  # False - because the second statement is false
print(3 < 2 and 4 < 3)  # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)  # False - because 3 > 2 is true, then not True gives False
print(not True)  # False - Negation, the not operator turns true to false
print(not False)  # True
print(not not True)  # True
print(not not False)  # False


"""
Output:
True
False
Addition:  4
Subtraction:  2
Multiplication:  9
Division:  1.0
Division:  1.5
Division:  1.75
Division without the remainder:  3
Division without the remainder:  2
Modulus:  1
Exponentiation:  27
Floating Point Number, PI 3.14
Floating Point Number, gravity 9.81
Complex number:  (1+1j)
Multiplying complex numbers:  (2+0j)
5
a + b =  5
a - b =  1
a * b =  6
a / b =  1.5
a % b =  1
a // b =  1
a ** b =  9
== Addition, Subtraction, Multiplication, Division, Modulus ==
total:  7
difference:  1
product:  12
division:  1.3333333333333333
remainder:  1
Area of a circle: 314.0
Area of rectangle: 200
735.75 N
True
True
False
True
True
False
True
False
True
True
False
True
True
False
True == True:  True
True == False:  False
False == False: True
1 is 1 True
1 is not 2 True
A in Muyiwa False
B in Muyiwa False
True
a in an: True
4 is 2 ** 2: True
True
False
False
True and True:  True
True
True
False
True or False: True
False
False
True
True
False

Process finished with exit code 0
"""