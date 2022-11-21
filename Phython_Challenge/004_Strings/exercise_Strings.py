#1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
space = ' '
concatenated_string  = 'Thirty' + space + 'Days' + space + 'Of' + space + 'Python'
print(concatenated_string)

#2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
concatenated_string  = 'Coding' + space + 'For' + space + 'All'
print(concatenated_string)

#3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

#4. Print the variable company using print().
print(company)

#5. Print the length of the company string using len() method and print().
print(len(company))

#6. Change all the characters to uppercase letters using upper() method.
print(company.upper())

#7. Change all the characters to lowercase letters using lower() method.
print(company.lower())

#8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#7. Cut(slice) out the first word of Coding For All string.
print("Coding For All"[:7])

#8. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(("Coding" in "Coding For All"))

#9. Replace the word coding in the string 'Coding For All' to Python.
print("Coding For All".replace("Coding", "Python"))

#10. Change Python for Everyone to Python for All using the replace method or other methods.
print("Python for Everyone".replace("Everyone", "All"))

#11. Split the string 'Coding For All' using space as the separator (split()) .
print('Coding For All'.split(" "))

#12. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", "))

#13. What is the character at index 0 in the string Coding For All.
print("Coding For All"[0])

#14. What is the last index of the string Coding For All.
print("Coding For All"[-1])

#15. What character is at index 10 in "Coding For All" string.
print("Coding For All"[10])

#16. Create an acronym or an abbreviation for the name 'Python For Everyone'.
print("".join([word[0] for word in 'Python For Everyone'.split(" ")]))

#17. Create an acronym or an abbreviation for the name 'Coding For All'.
print("".join([word[0] for word in 'Coding For All'.split(" ")]))

#18. Use index to determine the position of the first occurrence of C in Coding For All.
print("Coding For All".index("C"))

#19. Use index to determine the position of the first occurrence of C in Coding For All.
print("Coding For All".index("C"))

#20. Use index to determine the position of the first occurrence of F in Coding For All.
print("Coding For All".index("C"))

#21. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print("Coding For All People".rfind("l"))

#22. Use index or find to find the position of the first occurrence of the word 'because'
#   in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.find("because"))

#23. Use rindex to find the position of the last occurrence of the word because
#   in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.rfind("because"))

#24. Slice out the phrase 'because because because' in the following sentence:
#   'You cannot end a sentence with because because because is a conjunction'
print(" ".join([word for word in 'You cannot end a sentence with because because because is a conjunction'.split() \
                if word == "because"]))

#25. Find the position of the first occurrence of the word 'because' in the following sentence:
#   'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.index("because"))

#26. Slice out the phrase 'because because because' in the following sentence:
#   'You cannot end a sentence with because because because is a conjunction'
print(" ".join([word for word in 'You cannot end a sentence with because because because is a conjunction'.split() \
                if word == "because"]))

#27. Does ''Coding For All' start with a substring Coding?
print("'Coding For All".startswith("Coding"))

#28. Does 'Coding For All' end with a substring coding?
print("Coding For All".endswith("Coding"))

#29. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print('   Coding For All      '.strip("   "))

#30. Which one of the following variables return True when we use the method isidentifier():
#   30DaysOfPython
#   thirty_days_of_python
print([word for word in ["30DaysOfPython", "thirty_days_of_python"] if word.isidentifier() == True][0])

#31. The following list contains the names of some of python libraries:
#   ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
print("# ".join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

#32. Use the new line escape sequence to separate the following sentences.
#   I am enjoying this challenge.
#   I just wonder what is next.
print("I am enjoying this challenge.\nI just wonder what is next.")

#33. Use a tab escape sequence to write the following lines.
#   Name      Age     Country   City
#   Muyiwa  250     UK   London
print("IName\tAge\tCountry\tCity\nMuyiwa\t250\tUK\tLondon")

#34. Use the string formatting method to display the following:
#   radius = 10
#   area = 3.14 * radius ** 2
#   The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius %i is %i meters square" % (radius, area))

#7. Make the following using string formatting methods:
a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

"""
Output:
Thirty Days Of Python
Coding For All
Coding For All
14
CODING FOR ALL
coding for all
Coding for all
Coding For All
cODING fOR aLL
Coding 
True
Python For All
Python for All
['Coding', 'For', 'All']
['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
C
l
 
PFE
CFA
0
0
0
19
31
47
because because because
31
because because because
False
False
Coding For All
thirty_days_of_python
Django# Flask# Bottle# Pyramid# Falcon
I am enjoying this challenge.
I just wonder what is next.
IName	Age	Country	City
Muyiwa	250	UK	London
The area of a circle with radius 10 is 314 meters square
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144

Process finished with exit code 0
"""