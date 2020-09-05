print("Hello world")

# VARIABLES - a way store a single piece of data
# integer data type
score = 0 
health = 100
# string data type
name = "Zelda"

print(health)
print(score)
print("Hello " + name)

user = input("What is your name?")
print("Hello " + user)

# Ask the user for their favorite color. Then print out
# their favorite color.
color = input("What is your color?")
print("Awesome! " + color + " is a great color!")

# CONDITIONALS - if/else statements used for decision-making.
# tests if a condition is true, if so do a command else do something.

# if color == "blue":
#     print("the sky is blue!")
# elif color == "red":
#     print("roses are red")
# else:
#     print("idk what color that is")

if type(color) == str:
    print("Color is a string")

if isinstance(color, str):
    print("Color is an instance of a string")

num = 10

if isinstance(num, int):
    print("num is an integer")

 
