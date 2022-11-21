#Exercises: Level 1
#1.Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print(i)

i=0
while i < 11:
    print(i)
    i+=1

#2. Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10, -1, -1):
    print(i)

i = 10
while i > -1:
    print(i)
    i -= 1

#3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

hashtag = "#"
for i in range(1, 8):
    print(hashtag * i)

i = 1
hashtag = "#"
while i < 8:
    print(hashtag * i)
    i += 1

#4. Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

space = "        "
for x in range(len(space)):
    hashtag = space.replace(" ", " #")
    for y in range(1):  # need range(1) to loop exactly once
        print(hashtag)

#5. Print the following pattern:

for i in range(11):
    print("{} x {} = {}".format(i, i, i*i))

#6. Iterate through the list,
item_lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
#using a for loop and print out the items.
for item in item_lst:
    print(item)

#7. Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i % 2 == 0:
        print(i)

#8. Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i % 2 != 0:
        print(i)


# Exercises: Level 2
#1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum_num = 0
for i in range(101):
    sum_num += i
print(sum_num)
# The sum of all numbers is 5050.

#2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_even = 0
sum_odd = 0
for i in range(101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print("The sum of all evens is {}. And the sum of all odds is {}.".format(sum_even, sum_odd))
#The sum of all evens is 2550. And the sum of all odds is 2500.

#Exercises: Level 3
#1. Go to the data folder and use the countries.py file. Loop through the countries and
# extract all the countries containing the word land.

with open("C:\PythonPractises\Phython_Challenge\data\countries.py", errors="ignore") as f:
    # add item to the list
    countries = f.readlines()

for country in countries:
    if 'land' in country:
        print(country)

#2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
reverse_fruits = []
for i in range(1, len(fruits)+1):
    reverse_fruits.append(fruits[-i])
print(reverse_fruits)

#3. Go to the data folder and use the countries_data.py file.
#What are the total number of languages in the data
with open("C:\PythonPractises\Phython_Challenge\data\countries-data.py", errors="ignore") as f:
    file = f.readlines()

languages = []
for i, item in enumerate(file):
    if 'languages' in item:
        #print(str(i) + str(item))
        j = 1
        while ']' not in file[i+j]:
            languages.append(file[i+j])
            j += 1

languages = [lang.rstrip('",\n').lstrip('            "') for lang in languages]
print(languages)
print(len(languages))

#Find the ten most spoken languages from the data
distinct_language = set(languages)
language_dict = {lang : languages.count(lang) for lang in distinct_language}
sorted_language = dict(sorted(language_dict.items(), key=lambda item: item[1], reverse=True))
ten_most_spoken_languages = dict(list(sorted_language.items())[:10])
print(ten_most_spoken_languages)


"""
Output:
0
1
2
3
4
5
6
7
8
9
10
0
1
2
3
4
5
6
7
8
9
10
10
9
8
7
6
5
4
3
2
1
0
10
9
8
7
6
5
4
3
2
1
0
#
##
###
####
#####
######
#######
#
##
###
####
#####
######
#######
 # # # # # # # #
 # # # # # # # #
 # # # # # # # #
 # # # # # # # #
 # # # # # # # #
 # # # # # # # #
 # # # # # # # #
 # # # # # # # #
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
Python
Numpy
Pandas
Django
Flask
0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
51
53
55
57
59
61
63
65
67
69
71
73
75
77
79
81
83
85
87
89
91
93
95
97
99
5050
The sum of all evens is 2550. And the sum of all odds is 2500.
  'Finland',

  'Iceland',

  'Ireland',

  'Marshall Islands',

  'Netherlands',

  'New Zealand',

  'Poland',

  'Solomon Islands',

  'Swaziland',

  'Switzerland',

  'Thailand',

['lemon', 'mango', 'orange', 'banana']
['Pashto', 'Uzbek', 'Turkmen', 'Swedish', 'Albanian', 'Arabic', 'English', 'Samoan', 'Catalan', 'Portuguese', 'English', 'English', 'Russian', 'English', 'Spanish', 'GuaranÃ\xad', 'Armenian', 'Russian', 'Dutch', '(Eastern) Punjabi', 'English', 'German', 'Azerbaijani', 'English', 'Arabic', 'Bengali', 'English', 'Belarusian', 'Russian', 'Dutch', 'French', 'German', 'English', 'Spanish', 'French', 'English', 'Dzongkha', 'Spanish', 'Aymara', 'Quechua', 'Dutch', 'Bosnian', 'Croatian', 'Serbian', 'English', 'Tswana', 'Norwegian', 'Norwegian BokmÃ¥l', 'Norwegian Nynorsk', 'Portuguese', 'English', 'English', 'English', 'English', 'Malay', 'Bulgarian', 'French', 'Fula', 'French', 'Kirundi', 'Khmer', 'English', 'French', 'English', 'French', 'Portuguese', 'English', 'French', 'Sango', 'French', 'Arabic', 'Spanish', 'Chinese', 'English', 'English', 'Spanish', 'Arabic', 'French', 'French', 'Lingala', 'French', 'Lingala', 'Kongo', 'Swahili', 'Luba-Katanga', 'English', 'Spanish', 'Croatian', 'Spanish', 'Dutch', '(Eastern) Punjabi', 'English', 'Greek (modern)', 'Turkish', 'Armenian', 'Czech', 'Slovak', 'Danish', 'French', 'Arabic', 'English', 'Spanish', 'Spanish', 'Arabic', 'Spanish', 'Spanish', 'French', 'Tigrinya', 'Arabic', 'English', 'Estonian', 'Amharic', 'English', 'Faroese', 'English', 'Fijian', 'Hindi', 'Urdu', 'Finnish', 'Swedish', 'French', 'French', 'French', 'French', 'French', 'English', 'Georgian', 'German', 'English', 'English', 'Greek (modern)', 'Kalaallisut', 'English', 'French', 'English', 'Chamorro', 'Spanish', 'Spanish', 'English', 'French', 'French', 'Fula', 'Portuguese', 'English', 'French', 'Haitian', 'English', 'Latin', 'Italian', 'French', 'German', 'Spanish', 'English', 'Chinese', 'Hungarian', 'Icelandic', 'Hindi', 'English', 'Indonesian', 'French', 'Persian (Farsi)', 'Arabic', 'Kurdish', 'Irish', 'English', 'English', 'Manx', 'Hebrew (modern)', 'Arabic', 'Italian', 'English', 'Japanese', 'English', 'French', 'Arabic', 'Kazakh', 'Russian', 'English', 'Swahili', 'English', 'Arabic', 'Kyrgyz', 'Russian', 'Lao', 'Latvian', 'Arabic', 'French', 'English', 'Southern Sotho', 'English', 'Arabic', 'German', 'Lithuanian', 'French', 'German', 'Luxembourgish', 'Chinese', 'Portuguese', 'Macedonian', 'French', 'Malagasy', 'English', 'Chichewa', 'Malaysian', 'Divehi', 'French', 'Maltese', 'English', 'English', 'Marshallese', 'French', 'Arabic', 'English', 'French', 'Spanish', 'English', 'Romanian', 'French', 'Mongolian', 'Serbian', 'Bosnian', 'Albanian', 'Croatian', 'English', 'Arabic', 'Portuguese', 'Burmese', 'English', 'Afrikaans', 'English', 'Nauruan', 'Nepali', 'Dutch', 'French', 'English', 'MÄori', 'Spanish', 'French', 'English', 'English', 'English', 'Korean', 'English', 'Chamorro', 'Norwegian', 'Norwegian BokmÃ¥l', 'Norwegian Nynorsk', 'Arabic', 'English', 'Urdu', 'English', 'Arabic', 'Spanish', 'English', 'Spanish', 'GuaranÃ\xad', 'Spanish', 'English', 'English', 'Polish', 'Portuguese', 'Spanish', 'English', 'Arabic', 'Albanian', 'Serbian', 'French', 'Romanian', 'Russian', 'Kinyarwanda', 'English', 'French', 'French', 'English', 'English', 'English', 'English', 'French', 'Dutch', 'French', 'English', 'Samoan', 'English', 'Italian', 'Portuguese', 'Arabic', 'French', 'Serbian', 'French', 'English', 'English', 'English', 'Malay', 'Tamil', 'Chinese', 'Dutch', 'English', 'Slovak', 'Slovene', 'English', 'Somali', 'Arabic', 'Afrikaans', 'English', 'Southern Ndebele', 'Southern Sotho', 'Swati', 'Tswana', 'Tsonga', 'Venda', 'Xhosa', 'Zulu', 'English', 'Korean', 'English', 'Spanish', 'Sinhalese', 'Tamil', 'Arabic', 'English', 'Dutch', 'Norwegian', 'English', 'Swati', 'Swedish', 'German', 'French', 'Italian', 'Arabic', 'Chinese', 'Tajik', 'Russian', 'Swahili', 'English', 'Thai', 'Portuguese', 'French', 'English', 'English', 'Tonga (Tonga Islands)', 'English', 'Arabic', 'Turkish', 'Turkmen', 'Russian', 'English', 'English', 'English', 'Swahili', 'Ukrainian', 'Arabic', 'English', 'English', 'Spanish', 'Uzbek', 'Russian', 'Bislama', 'English', 'French', 'Spanish', 'Vietnamese', 'French', 'Spanish', 'Arabic', 'English', 'English', 'Shona', 'Northern Ndebele']
368
{'English': 91, 'French': 45, 'Arabic': 25, 'Spanish': 24, 'Russian': 9, 'Portuguese': 9, 'Dutch': 8, 'German': 7, 'Chinese': 5, 'Italian': 4}

Process finished with exit code 0
"""