countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Muyiwa', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Explain the difference between map, filter, and reduce.
# Map is used to operate on an iterable i.e. return the value of a function operation on a list while
# filter is used to check if the condition of a function is true while reduce an reduces an iterable based on the operation of a function.

# 4 Use for loop to print each country in the countries list.
for i in countries:
    print(i)
# 5 Use for to print each name in the names list.
for i in names:
    print(i)
# 6 Use for to print each number in the numbers list.
for i in names:
    print(i)

# Exercise level 2
# 1 Use map to create a new list by changing each country to uppercase in the countries list
upper_countries = map(lambda x: x.upper(), countries)
print(list(upper_countries))

# 2 Use map to create a new list by changing each number to its square in the numbers list
sq_numbers = map(lambda x: x ** 2, numbers)
print(list(sq_numbers))

# 3 Use map to change each name to uppercase in the names list
upper_names = map(lambda x: x.upper(), names)
print(list(upper_names))

# 4 Use filter to filter out countries containing 'land'.
filter_countries = filter(lambda x: 'land' in x, countries)
print(list(filter_countries))

# 5 Use filter to filter out countries having exactly six characters.
filter_countries = filter(lambda x: (len(x) == 6), countries)
print(list(filter_countries))

# 6 Use filter to filter out countries containing six letters and more in the country list.
filter_countries = filter(lambda x: (len(x) >= 6), countries)
print(list(filter_countries))

# 7 Use filter to filter out countries starting with an 'E'
filter_countries = filter(lambda x: x.startswith('E'), countries)
print(list(filter_countries))

# 8 Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce

chain_high = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, numbers)))
print(chain_high)

# 9 Declare a function called get_string_lists which takes a list as a parameter and
# then returns a list containing only string items.
li = [2, 2, 3, 4, 'ghg', 'fgf']
get_strings_lists = filter(lambda x: type(x) == type('string'), li)
print(list(get_strings_lists))

# 10 Use reduce to sum all the numbers in the numbers list.
sum_red = reduce(lambda x, y: x + y, numbers)
print(sum_red)

# 11 Use reduce to concatenate all the countries and to produce this sentence:
# Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
nec = 'are north european countries'
concat_reduce = reduce(lambda x, nec: x + ', ' + nec, countries)
print(concat_reduce)


# 12 Declare a function called categorize_countries that returns a list of countries with some common pattern
# (you can find the countries list in this repository as countries.json(eg 'land', 'ia', 'island', 'stan')).

def categorize_countries(country):
    countries_list = []
    for name in country:
        if 'land' in country or 'ia' in country or 'island' in country or 'stan' in country:
            countries_list.append(name)
    return countries_list


# 13 Create a function returning a dictionary, where keys stand for starting letters of countries and
# values are the number of country names starting with that letter.
def create_country_dict(country):
    country_dict = {}
    for name in country:
        first_letter = name[0]
        country_dict[first_letter] = [name for name in country if name[0] == first_letter].count()
    return country_dict

# 14 Declare a get_first_ten_countries function - it returns a list of first ten countries
# from the countries.js list in the data folder.


def get_first_ten_countries(countries_list):
    return countries_list[:10]

# 15 Declare a get_last_ten_countries function that returns the last ten countries in the countries list.


def get_last_ten_countries(countries_list):
    return countries_list[-10:]

"""
Output:
Estonia
Finland
Sweden
Denmark
Norway
Iceland
Muyiwa
Lidiya
Ermias
Abraham
Muyiwa
Lidiya
Ermias
Abraham
['ESTONIA', 'FINLAND', 'SWEDEN', 'DENMARK', 'NORWAY', 'ICELAND']
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
['MUYIWA', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
['Finland', 'Iceland']
['Sweden', 'Norway']
['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
['Estonia']
220
['ghg', 'fgf']
55
Estonia, Finland, Sweden, Denmark, Norway, Iceland

Process finished with exit code 0
"""