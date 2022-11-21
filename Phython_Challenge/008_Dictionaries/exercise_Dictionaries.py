# Exercises: Day 8
#1. Create an empty dictionary called dog
dog = {}

#2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Murphy'
dog['color'] = 'brown'
dog['breed'] = 'rottweiler'
dog['legs'] = 'short'
dog['age'] = '5'

#3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills,
#  country, city and address as keys for the dictionary
student = {'first_name':'James',
           'last_name':'Trump',
           'gender':'male',
           'age':'25',
           'marital_status':'single',
           'skills':['programming', 'communication','research'],
           'country':'Ireland',
           'city':'Dublin',
           'address':'1008 White Lane'}

#4. Get the length of the student dictionary
print(len(student))

#5. Get the value of skills and check the data type, it should be a list
print(type(student.get('skills')))

#5. Modify the skills values by adding one or two skills
student['skills'].append('presentation')
print(student)

#6. Get the dictionary keys as a list
print(list(student.keys()))

#7. Get the dictionary values as a list
print([value for key, value in student.items()])

#8. Change the dictionary to a list of tuples using items() method
print([(key, value) for key, value in student.items()])

#9 Delete one of the items in the dictionary
student.pop('first_name')

#10 Delete one of the dictionaries
del student

"""
Output:
9
<class 'list'>
{'first_name': 'James', 'last_name': 'Trump', 'gender': 'male', 'age': '25', 'marital_status': 'single', 'skills': ['programming', 'communication', 'research', 'presentation'], 'country': 'Ireland', 'city': 'Dublin', 'address': '1008 White Lane'}
['first_name', 'last_name', 'gender', 'age', 'marital_status', 'skills', 'country', 'city', 'address']
['James', 'Trump', 'male', '25', 'single', ['programming', 'communication', 'research', 'presentation'], 'Ireland', 'Dublin', '1008 White Lane']
[('first_name', 'James'), ('last_name', 'Trump'), ('gender', 'male'), ('age', '25'), ('marital_status', 'single'), ('skills', ['programming', 'communication', 'research', 'presentation']), ('country', 'Ireland'), ('city', 'Dublin'), ('address', '1008 White Lane')]

Process finished with exit code 0
"""