#Exercises: Level 1
#1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    return a + b

#2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    pi = 3.14
    return  pi * r * r

#3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*numbers):
    total = 0
    for i in numbers:
        if type(numbers) == int or type(numbers) == float:
            total += i
    return total
print(add_all_nums(1,2,3,4,5))

#4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

#5. Write a function called check-season, it takes a month parameter and
# returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):

    if month in ['September', 'October', 'November']:
        return 'Autumn'
    elif month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    else:
        return 'Summer'

#6. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1)/(x2 - x1)

#7. Quadratic equation is calculated as follows: ax² + bx + c = 0.
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b, c):
    x1 = (-b + (b**2 - 4*a*c) ** 0.5)/2*a
    x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
    return x1, x2

#8. Declare a function named print_list. It takes a list as a parameter and
# it prints out each element of the list.
def print_list(samplelst):
    for item in samplelst:
        print(item)

#9. Declare a function named reverse_list. It takes an array as a parameter and
# it returns the reverse of the array (use loops).
def reverse_list(item_lst):
    number_lst = []
    for i, num in enumerate(item_lst):
        while len(number_lst) < len(item_lst):
            number_lst.append(item_lst[-(i+1)])
            i += 1
    return number_lst

print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]

#10. Declare a function named capitalize_list_items.
# It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(item_lst):
    output_lst = []
    for item in item_lst:
        output_lst.append(item.upper())
    return output_lst

print(capitalize_list_items(["Muyiwa", "Tema", "John", "Matthew"]))

#10. Declare a function named add_item. It takes a list and an item parameters.
# It returns a list with the item added at the end.
def add_item(item_lst, item):
    return item_lst.append(item)

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      #[2, 3, 7, 9, 5]

#11 Declare a function named remove_item. It takes a list and an item parameters.
# It returns a list with the item removed from it.
def remove_item(item_lst, item):
    return item_lst.remove(item)

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]

#12 Declare a function named sum_of_numbers.
# It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(number):
    item_lst = range(1, number + 1)
    total = 0
    for item in item_lst:
        total += item
    return total

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

#13. Declare a function named sum_of_odds. It takes a number parameter
# and it adds all the odd numbers in that range.
def sum_of_odds(number):
    item_lst = range(1, number + 1)
    total = 0
    for item in item_lst:
        if item % 2 != 0:
            total += item
    return total

print(sum_of_odds(10)) # 55

#14. Declare a function named sum_of_even. It takes a number parameter
# and it adds all the even numbers in that - range.
def sum_of_even(number):
    item_lst = range(1, number + 1)
    total = 0
    for item in item_lst:
        if item % 2 == 0:
            total += item
    return total

print(sum_of_even(10)) # 55

# Exercises: Level 2
#1. Declare a function named evens_and_odds .
# It takes a positive integer as parameter and
# it counts number of evens and odds in the number.
def evens_and_odds(number):
    item_lst = range(number + 1)
    print(list(item_lst))
    odd_lst = []
    even_lst = []
    for item in item_lst:
        if item % 2 != 0:
            odd_lst.append(item)
        else:
            even_lst.append(item)
    print("The number of odds are %i" % (len(odd_lst)))
    print("The number of evens are %i" % (len(even_lst)))
    # The number of odds are 50.
    # The number of evens are 51.

#2. Call your function factorial, it takes a whole number as a parameter
# and it return a factorial of the number
def get_factorial(num):
    factorial = 1
    # check if the number is negative, positive or zero
    if num < 0:
       print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
       print("The factorial of 0 is 1")
    else:
       for i in range(1, num + 1):
           factorial = factorial*i
       return factorial

#3. Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(checklst):
    if len(checklst) != 0:
        return "Not empty"
    else:
        return "It's empty"

#4.Write different functions which take lists. They should calculate_mean,
# calculate_median, calculate_mode, calculate_range, calculate_variance,
# calculate_std (standard deviation).
def calculate_mean(lists):
    return sum(lists)/len(lists)

def calculate_median(lists):
    lists.sort()
    mid = len(lists) // 2
    res = (lists[mid] + lists[~mid]) / 2
    return res

def calculate_mode(lists):
    # dictionary to keep count of each value
    counts = {}
    # iterate through the list
    for item in lists:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    # get the keys with the max counts
    res = [key for key in counts.keys() if counts[key] == max(counts.values())]
    if len(res) == 1:
        return res[0]
    else:
        return res

def calculate_range(lists):
    return max(lists) - min(lists)

def calculate_variance(lists):
    return max(lists) - min(lists)

def calculate_variance(lists):
    deviations = [(num - calculate_mean(lists)) ** 2 for num in lists]
    variance = sum(deviations) / len(lists)
    return variance

def calculated_std(lists):
    return calculate_variance(lists) ** 0.5

#Exercises: Level 3
#Write a function called is_prime, which checks if a number is prime.

def is_prime(num):
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        print(num, "is not a prime number")

is_prime(31)


#1. Write a functions which checks if all items are unique in the list.

def check_list(lists):
    if len(set(lists)) == len(lists):
       print("All elements are unique.")
    else:
       print("All elements are not unique.")

check_list([2, 3, 4, 4, 7])

#2.Write a function which checks if all the items of the list are of the same data type.

def check_same_type(lists):
    type_lst = []
    for item in lists:
        type_lst.append(type(item))
    if len(set(type_lst)) == 1:
        print("They are of the same data type (%s)" % type_lst[0])
    else:
        print("They are not of the same data type")
check_same_type([2, 6, 7, 3, 3])


#Write a function which check if provided variable is a valid python variable
#Go to the data folder and access the countries-data.py file.
with open("C:\PythonPractises\Phython_Challenge\data\countries-data.py",
          errors="ignore") as f:
    file = f.readlines()


#Create a function called the most_spoken_languages in the world.
# It should return 10 or 20 most spoken languages in the world in descending order
def most_spoken_languages(file_lst, num):

    languages = []
    for i, item in enumerate(file_lst):
        if 'languages' in item:
            #print(str(i) + str(item))
            j = 1
            while ']' not in file_lst[i+j]:
                languages.append(file_lst[i+j])
                j += 1

    languages = [lang.rstrip('",\n').lstrip('            "') for lang in languages]
    distinct_language = set(languages)
    language_dict = {lang : languages.count(lang) for lang in distinct_language}
    sorted_language = dict(sorted(language_dict.items(), key=lambda item: item[1], reverse=True))
    most_spoken_languages = dict(list(sorted_language.items())[:num])
    return most_spoken_languages

#Create a function called the most_populated_countries.
# It should return 10 or 20 most populated countries in descending order.