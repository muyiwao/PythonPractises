# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Exercises: Level 1
#1. Find the length of the set it_companies
print(len(it_companies))

#2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#3. Insert multiple IT companies at once to the set it_companies
it_companies.update({'Huawei', 'Linux', 'Solaris'})
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove('Huawei')
print(it_companies)

#What is the difference between remove and discard
"""
the remove() method will raise an error if the specified item does not exist, and 
the discard() method will not.
"""

# Exercises: Level 2
#1. Join A and B
A.update(B)
print(A)

#2. Find A intersection B
A.intersection(B)
print(A)

#3. Is A subset of B
print(A.issubset(B))

#4. Are A and B disjoint sets
print(A.isdisjoint(B))

#5. Join A with B and B with A
A.update(B)
print(A)

B.update(A)
print(B)

#6. What is the symmetric difference between A and B
"""It means that it returns a set that contains all items from set A amd B"""

#7. Delete the sets completely
del A, B


# Exercises: Level 3
#1 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_st = set(age)
if len(age) > len(age_st):
    print("length of the list is greater than set")
else:
    print("length of the list is less than set")

#2. Explain the difference between the following data types: string, list, tuple and set
"""string is a sequence of unicode characters with quotation marks on either side of the sequence.
Lists and tuples are like arrays. 
Tuples like strings are immutables. 
Lists are mutable so they can be extended or reduced at will. 
Sets are mutable unordered sequence of unique elements """

#3. I am a teacher and I love to inspire and teach people.
# How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
split_word = sentence.split(" ")
unique_word = set(split_word)
print(len(unique_word))

"""
Output:
7
{'Amazon', 'Google', 'Microsoft', 'Oracle', 'IBM', 'Apple', 'Twitter', 'Facebook'}
{'Amazon', 'Google', 'Linux', 'Huawei', 'Microsoft', 'Oracle', 'Solaris', 'IBM', 'Apple', 'Twitter', 'Facebook'}
{'Amazon', 'Google', 'Linux', 'Microsoft', 'Oracle', 'Solaris', 'IBM', 'Apple', 'Twitter', 'Facebook'}
{19, 20, 22, 24, 25, 26, 27, 28}
{19, 20, 22, 24, 25, 26, 27, 28}
True
False
{19, 20, 22, 24, 25, 26, 27, 28}
{19, 20, 22, 24, 25, 26, 27, 28}
length of the list is greater than set
10
"""