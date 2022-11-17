#   Exercise

#   1.Declare your age as integer variable
age = 50

#   2.Declare your height as a float variable
height = 6.5

#   3.Declare a variable that store a complex number
complex_var = 1 + 3j

#   4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base_value = float(input("Enter base: "))
height_value = float(input("Enter height: "))
area_of_triangle = 0.5 * base_value * height_value
print("The area of the triangle is ", int(area_of_triangle))

#   5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter_of_triangle = side_a + side_b + side_c
print("The perimeter of the triangle is ", perimeter_of_triangle)

#   6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)
print("The area of the rectangle is ", area_of_rectangle)
print("The perimeter of the rectangle is ", perimeter_of_rectangle)

#   7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input("Enter radius: "))
pi = 3.14
area_of_circle = pi * radius * radius
circumference_of_circle = 2 * pi * radius
print("The area of the circle is ", area_of_circle)
print("The circumference of the circle is ", circumference_of_circle)

#   8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
x = 0
y_intercept = 2 * x - 2

y = 0
x_intercept = (y + 2) / 2

slope = (y - y_intercept) / (x_intercept - x)
print("The slope is ", slope)
print("The x-intercept is ", x_intercept)
print("The y-intercept is ", y_intercept)

#   9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
m = (y2 - y1) / (x2 - x1)
d = (((y1 - x1) ** 2) + ((y2 - x2) ** 2)) ** 0.5
print("The slope is ", m)
print("The Euclidean distance is ", d)

#   10. Compare the slopes in tasks 8 and 9.
if slope > m:
    print("slope in task 8 is greater than slope in task 9")
else:
    print("slope in task 8 is less than slope in task 9")

#   11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
proceed = True
while proceed:
    x = int(input("Enter the value of x: "))
    y = (x ** 2) + (6 * x) + 9
    if y == 0:
        print("y is zero when x is ", x)
        proceed = False

#   12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python = "python"
dragon = "dragon"
print(len(python) > len(dragon))

#   13 Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in python and 'on' in dragon)

#   14 I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("jargon" in "I hope this course is not full of jargon")

#   15 There is no 'on' in both dragon and python
print('on' not in python and 'on' not in dragon)

#   16 Find the length of the text python and convert the value to float and convert it to string
(text_len) = len(python)
f_text_len = float(text_len)
s_text_len = str(text_len)

#   17 Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not
#   using python? using %

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is not even")

#   18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_div = 7 // 3
number = 2.7
if floor_div == int(number):
    print("floor division of 7 by 3 is equal to the int converted value of 2.7")
else:
    print("floor division of 7 by 3 is not equal to the int converted value of 2.7")

#   19 Check if type of '10' is equal to type of 10
if type('10') == type(10):
    print("type of '10' is equal to type of 10")
else:
    print("type of '10' is not equal to type of 10")

#   20 Check if int('9.8') is equal to 10
"""
if int('9.8') == 10:
    print("int('9.8') is equal to 10")
else:
    print("int('9.8') is not equal to 10")
"""

#   21 Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input("Enter hours: "))
rate = int(input("Enter rate per hours: "))
pay = hours * rate
print("The pay of the personis: ", pay)

#   22 Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print("The number of seconds a person can live is ", seconds)

#   23 Write a Python script that displays the following table
print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)


"""
Output:
Enter base: 20
Enter height: 10
The area of the triangle is  100
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is  12.0
Enter length: 10
Enter width: 15
The area of the rectangle is  150.0
The perimeter of the rectangle is  50.0
Enter radius: 5
The area of the circle is  78.5
The circumference of the circle is  31.400000000000002
The slope is  2.0
The x-intercept is  1.0
The y-intercept is  -2
The slope is  2.0
The Euclidean distance is  4.0
slope in task 8 is less than slope in task 9
Enter the value of x: 3
Enter the value of x: 1
Enter the value of x: -3
y is zero when x is  -3
False
True
True
False
Enter a number: 20
Number is even
floor division of 7 by 3 is equal to the int converted value of 2.7
type of '10' is not equal to type of 10
Enter hours: 8
Enter rate per hours: 100
The pay of the personis:  800
Enter number of years you have lived: 100
The number of seconds a person can live is  3153600000
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125

Process finished with exit code 0


"""