#   Exercises: Level 1

#   Declare an empty list
empty_list = []

#   Declare a list with more than 5 items
item_list = ["pawpaw", "grape", "banana", "orange", "strawberry", "lime"]

#   Find the length of your list
print(len(item_list))

#   Get the first item, the middle item and the last item of the list
first_item = item_list[0]
middle_item = item_list[len(item_list) / 2]
last_item = item_list[-1]

#   Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Muyiwa', '250', 'Married', '10 Malt Street']

#   Declare a list variable named it_companies and assign initial values
#   Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#   Print the list using print()
print(it_companies)

#   Print the number of companies in the list
print(len(it_companies))

#   Print the first, middle and last company
print(it_companies[0])
print(it_companies[int(len(it_companies) / 2)])
print(it_companies[-1])

#   Print the list after modifying one of the companies
it_companies[1] = 'Alphabet'
print(it_companies)

#   Add an IT company to it_companies
it_companies.append('Linux')
print(it_companies)

#   Insert an IT company in the middle of the companies list
it_companies.insert(int(len(it_companies) / 2), "Huawei")
print(it_companies)

#   Change one of the it_companies names to uppercase (IBM excluded!)
print([company.upper() for company in it_companies if company != 'IBM'])

#   Join the it_companies with a string '#;  '
print('#;  '.join(it_companies))

#   Check if a certain company exists in the it_companies list.
print('Apple' in it_companies)

#   Sort the list using sort() method
print(sorted(it_companies))

#   Reverse the list in descending order using reverse() method
print(it_companies.reverse())

#   Slice out the first 3 companies from the list
print(it_companies[:3])

#   Slice out the last 3 companies from the list
print(it_companies[-3:])

#   Slice out the middle IT company or companies from the list
print(it_companies[int(len(it_companies)/2)])

#   Remove the first IT company from the list
print(it_companies.remove(it_companies[0]))

#   Remove the middle IT company or companies from the list
it_companies.remove(it_companies[0])     # removes Facebook
print(it_companies)

#   Remove the last IT company from the list
it_companies.remove(it_companies[-1])

#   Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#   Destroy the IT companies list
del it_companies

#   Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
join_list = front_end + back_end
print(join_list)

#   After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack.
#   Then insert Python and SQL after Redux.
full_stack = join_list.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)


#   Exercises: Level 2
#   The following is a list of 10 students ages:
#   ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#   Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(sorted(ages))
minimum_age = min(ages)
maximum_age = max(ages)
print("Minimum age: %i" % minimum_age)
print("Maximum age: %i" % maximum_age)

#   Add the min age and the max age again to the list
ages.append(minimum_age)
ages.append(maximum_age)
print(ages)

#   Find the median age (one middle item or two middle items divided by two)
median_age = 0
list_length = len(ages)
if list_length % 2 == 0:
    first_number = ages[int(list_length/2)-1]
    second_number = ages[-int(list_length/2)]
    #   print(first_number, second_number)
    median_age = (first_number + second_number)/2

else:
    median_age = ages[int(list_length / 2)]

print(median_age)


#   Find the average age (sum of all items divided by their number )
sum_age = sum(ages)
average_age = sum_age/list_length
print(average_age)

#   Find the range of the ages (max minus min)
range_age = max(ages) - min(ages)
print(range_age)

#   Compare the value of (min - average) and (max - average), use abs() method
min_average_age = abs(min(ages) - average_age)
max_average_age = abs(max(ages) - average_age)
print(min_average_age < max_average_age)

#   Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

median_country = 0
countries_length = len(countries)
median_country = countries[int(countries_length / 2)]
print(median_country)

#   Divide the countries list into two equal lists if it is even if not one more country for the first half.
if countries_length % 2 == 0:
    print(countries[:countries_length/2])
else:
    first_half = countries[:int(countries_length/2)]
    first_half.append('Ireland')
    second_half = countries[int(countries_length/2):]
print(first_half)
print(second_half)

#   Unpack the first three countries and the rest as scandic countries.
first_three_countries = countries[:3]
scandic_countries = countries[3:]
print(first_three_countries)
print(scandic_countries)