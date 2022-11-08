def title(name):
    print(name)  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    title("Practise_31_10_2022")

    print("Hello World")

    # Drawing a Shape
    print('\n')
    print("Drawing a Shape")
    print("   /|")
    print("  / |")
    print(" /  |")
    print("/___| ")

    #  Variables and Data Types
    print('\n')
    print("Variables and Data Types")

    character_name = "John"
    character_age = "35"
    print("There once was a man named " + character_name + ", ")
    print("he was " + character_age + "years old. ")
    print("He really liked the name " + character_name + ", ")
    print("but didn't like being " + character_age + ".")

    #  Working with Strings
    print('\n')
    print("Working with Strings")

    print('Playing Ground')
    print('Playing\nGround')
    phrase = "Playing Ground"
    print(phrase)
    print(phrase.lower())
    print(phrase.upper())
    print(phrase.isupper())
    print(phrase.upper().isupper())
    print(len(phrase))
    print(phrase[3])
    print(phrase.index("G"))
    print(phrase.index("Gro"))
    print(phrase.index("z"))


    """
    
    Output
    
    Hello World
    
    Drawing a Shape
       /|
      / |
     /  |
    /___| 
    
    Variables and Data Types
    There once was a man named John, 
    he was 35years old. 
    He really liked the name John, 
    but didn't like being 35.
    
    Working with Strings
    Playing Ground
    Playing
    Ground
    Playing Ground
    playing ground
    PLAYING GROUND
    False
    True
    14
    y
    8
    8
    Traceback (most recent call last):
      File "C:\Users\kanzo\PycharmProjects\FirstProject\Practise_31_10_2022.py", line 45, in <module>
        print(phrase.index("z"))
    ValueError: substring not found
    
    Process finished with exit code 1

    """