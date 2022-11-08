from math import *


def title(name):
    print(name)  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    title("Practise_1_11_2022")

    # Working With Numbers
    print("Working With Numbers")
    print(2)
    print(3 * 4 + 5)
    print(3 * (4 + 5))
    print(10 % 3)
    my_num = 5
    print(str(my_num) + " my favourite number")
    print(pow(4, 6))
    print(max(4, 6))
    print(round(3.7))

    print(sqrt(36))

    # Getting input from users
    print("\n")
    print("Getting input from users")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print("Hello " + name + "!" + " You are " + age)


    # Building a Basic Calculator
    print("\n")
    print("Building a Basic Calculator")
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    result = int(num1) + int(num2)
    print(result)


    #  Mad Libs Game
    print("\n")
    print("Mad Libs Game")

    color = input("Enter a color: ")
    plural_noun = input("Enter a plural Noun: ")
    celebrity = input("Enter a celebrity: ")

    print("Roses are " + color)
    print(plural_noun + " are blue")
    print("I love " + celebrity)

    # Lists
    print("\n")
    print("Lists")
    friends = ["Kelvin", "Karen", "Jim"]
    friends[1] = "Mike"
    print(friends[1:])

    #  List Functions
    print("\n")
    print(" List Functions")
    lucky_numbers = [4, 8, 15, 16, 23, 42]
    friends = ["Kelvin", "Karen", "Jim", "Oscar", "Toby"]
    print(lucky_numbers.reverse())
    print(friends.index("Kelvin"))

    #   Tuples
    print("\n")
    print("  Tuples")

    coordinates = (4, 5)    # immutable
    coordinates[1] = 10
    print(coordinates[1])

    #   Functions
    print("\n")
    print("  Tuples")


    def sayhi(name1, age1):
        print("Hello " + name1 + ", you are " + str(age1))

    print("Top")
    sayhi("Mike", 35)
    print("Bottom")


    #   Return Statement
    print("\n")
    print(" Return Statement")

    def cube(num):
        return num*num*num

    result = cube(4)
    print(result)

    """
    Output:
        
    Practise_1_11_2022
    Working With Numbers
    2
    17
    27
    1
    5 my favourite number
    4096.0
    6
    4
    6.0
    
    Getting input from users
    Enter your name: Mike
    Enter your age: 30
    Hello Mike! You are 30
    
    Building a Basic Calculator
    Enter a number: 15
    Enter another number: 9
    24
    
    Mad Libs Game
    Enter a color: Blue
    Enter a plural Noun: Magenta
    Enter a celebrity: Hanks
    Roses are Blue
    Magenta are blue
    I love Hanks
      
    Lists
    ['Mike', 'Jim']
    
     List Functions
    None
    0
    
      Tuples
    Traceback (most recent call last):
      File "C:\Users\kanzo\PycharmProjects\FirstProject\Practise_1_11_2022.py", line 74, in <module>
        coordinates[1] = 10
    TypeError: 'tuple' object does not support item assignment
    
    Process finished with exit code 1

    
    
    
    """



