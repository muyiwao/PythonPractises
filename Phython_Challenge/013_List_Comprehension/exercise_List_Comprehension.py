# 1 Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filter_nums = [i for i in numbers if i <= 0]
print(filter_nums)

# 2 Flatten the following list of lists to a one dimensional list :
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
output = [num for row in list_of_lists for i in row for num in i]
print(output)

# 3 Using list comprehension create the following list of tuples:
rand_list = [(i, 1, i, (i * i), (i ** 3), (i ** 4), (i ** 5)) for i in range(11)]
print(rand_list)

# 4 Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat_countries = [list(country) for item in countries for country in item]
[item.insert(1, (flat_countries[0][0][0:3])) for item in flat_countries]
print(flat_countries)

# 5 Change the following list to a list of dictionaries:
key_list = ["country", "city"]
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_countries = [{key_list[0]: country[0], key_list[1]: country[1]} for row in countries for country in row]
print(dict_countries)

# 6 Change the following list of lists to a list of concatenated strings:
names = [[('Muyiwa', 'Oladimeji')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names_list = [name[0] + " " + name[1] for item in names for name in item]
print(names_list)

# 7 Write a lambda function which can solve a slope or y-intercept of linear functions.
x = 0
y = lambda m, b: (m * x) + b
print(y(2, 4))


"""
Output:
[-4, -3, -2, -1, 0]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[(0, 1, 0, 0, 0, 0, 0), (1, 1, 1, 1, 1, 1, 1), (2, 1, 2, 4, 8, 16, 32), (3, 1, 3, 9, 27, 81, 243), (4, 1, 4, 16, 64, 256, 1024), (5, 1, 5, 25, 125, 625, 3125), (6, 1, 6, 36, 216, 1296, 7776), (7, 1, 7, 49, 343, 2401, 16807), (8, 1, 8, 64, 512, 4096, 32768), (9, 1, 9, 81, 729, 6561, 59049), (10, 1, 10, 100, 1000, 10000, 100000)]
[['Finland', 'Fin', 'Helsinki'], ['Sweden', 'Fin', 'Stockholm'], ['Norway', 'Fin', 'Oslo']]
[{'country': 'Finland', 'city': 'Helsinki'}, {'country': 'Sweden', 'city': 'Stockholm'}, {'country': 'Norway', 'city': 'Oslo'}]
['Muyiwa Oladimeji', 'David Smith', 'Donald Trump', 'Bill Gates']
4

Process finished with exit code 0

"""
