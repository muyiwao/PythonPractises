# Exercise
# 1. Write a function which generates a six digit/character random_user_id.
#  print(random_user_id());
#  '1ee33d'

import random
import string


def random_user_id():
    # choose from all lowercase letter
    letters = string.ascii_lowercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(6))
    return result_str


print(random_user_id())


# 2. Modify the previous task. Declare a function named user_id_gen_by_user.
# It does’t take any parameters, but it takes two inputs using input().
# One of the inputs is the number of characters and the second input is the
# number of IDs which are supposed to be generated.

def user_id_gen_by_user(character_count, id_count):
    # choose from all lowercase letter
    id = "#"
    for i in range(id_count):
        for j in range(character_count):
            letter = random.choice(string.ascii_lowercase + string.digits)
            id += letter
        print(id)
        id = "#"


user_id_gen_by_user(5, 5)
user_id_gen_by_user(16, 5)


# 3. Write a function named rgb_color_gen.
# It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    rgb = ""
    for i in range(3):
        num = random.choice([str(j) for j in list(range(256))])
        rgb += num
        if i < 2:
            rgb += ","

    res = "rgb(" + rgb + ")"
    return res


print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form

"""
Exercises: Level 2
Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
Write a function generate_colors which can generate any number of hexa or rgb colors.
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b']
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
Exercises: Level 3
Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
"""


"""
Output:
22o50h
#ci1tt
#ecy7v
#a7sjg
#c5qk8
#f38rh
#jll8t0llanuk5v0c
#l9gzejau3k6kkuem
#lh57mfd6ur2vqqbl
#d87m7foedm9iqgf6
#hja8fw4aqle4f4k2
rgb(43,238,76)

Process finished with exit code 0

"""
