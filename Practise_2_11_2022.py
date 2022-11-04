# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("------Tutorial Practise for 2/11/2022------")

is_male = True
is_tall = True

# if condition
if is_male or is_tall:
    print("You are a male or tall or both")
elif is_male and not (is_tall):
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are not a male bu are tall")
else:
    print("You are neither male or tall")


# If Statements & Comparisons
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(3, 40, 5))

# Building a better Calculator
"""
num4 = float(input("Enter first number: "))
op = input("Enter operator: ")
num5 = float(input("enter second number: "))


if op == "+":
    print(num4 + num5)
elif op == "-":
    print(num4 - num5)
elif op == "/":
    print(num4 + num5)
elif op == "*":
    print(num4 * num5)
else:
    print("Invalid Operator")
"""

# Dictionaries
monthConversions = {"Jan": "January",
                    "Feb": "February",
                    "Mar": "March",
                    "Apr": "April",
                    "May": "May",
                    "Jun": "June",
                    "Jul": "July",
                    "Aug": "August",
                    "Sep": "September",
                    "Oct": "October",
                    "Nov": "November",
                    "Dec": "December"}
print(monthConversions["Nov"])
print(monthConversions.get("Luv", "Not a valid Key"))

# While Loop
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")

# Building a Guessing Game
"""
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses: You LOSE!")
else:
    print("You win!")
"""

#   For Loops
friends = ["Jim", "karen", "Kevin"]
for friend in friends:
    print(friend)

for index in range(5):
    if index == 0:
        print('First iteration')
    else:
        print("Not first iteration")


# Exponent Function

def raise_to_power(base_num, pow_num):
    result = 1
    for ij in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(2, 3))

# 2D Lists & Nested Loops
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[2][1])

for row in number_grid:
    print(row)
