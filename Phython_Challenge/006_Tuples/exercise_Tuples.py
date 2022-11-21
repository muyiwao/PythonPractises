#Exercises: Level 1
#1. Create an empty tuple
empty_tuple = ()

#2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Grace', 'Anne', 'Esther')
brothers = ('James', 'John')

#3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)

#4. How many siblings do you have?
print(len(siblings))

#4. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('Mathew', 'Liz')
print(family_members)


#Exercises: Level 2
#1. Unpack siblings and parents from family_members
siblings = family_members[:-2]
parents = family_members[-2:]
print(siblings)
print(parents)

#2. Create fruits, vegetables and animal products tuples. Join the three tuples and
# assign it to a variable called food_stuff_tp.
fruits = ('orange', 'banana', 'pawpaw', 'apple')
vegetables = ('spinach', 'brocolli', 'carrot')
animal_products = ('egg', 'meat', 'fat', 'gelatin')
food_stuff_tp = fruits + vegetables + animal_products

#3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff_lt_length = len(food_stuff_lt)
print(food_stuff_lt[:food_stuff_lt_length//2])

#5. Slice out the first three items and the last three items from food_staff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
print(first_three_items)
print(last_three_items)

#6. Delete the food_staff_tp tuple completely
del food_stuff_tp

#7. Check if an item exists in tuple:
#Check if 'Estonia' is a nordic country
#Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)

"""
Output:
'James', 'John', 'Grace', 'Anne', 'Esther')
5
('James', 'John', 'Grace', 'Anne', 'Esther', 'Mathew', 'Liz')
('James', 'John', 'Grace', 'Anne', 'Esther')
('Mathew', 'Liz')
['orange', 'banana', 'pawpaw', 'apple', 'spinach', 'brocolli', 'carrot', 'egg', 'meat', 'fat', 'gelatin']
['orange', 'banana', 'pawpaw', 'apple', 'spinach']
['orange', 'banana', 'pawpaw']
['meat', 'fat', 'gelatin']
False
True

Process finished with exit code 0
"""



