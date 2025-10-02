# -------------------------------------------
# Exercise 0: Revision on Variables & Input
# -------------------------------------------
# This exercise will help you practice:
# - Creating and naming multiple variables
# - Taking user input
# - Printing output using variables
# - Using f-strings to combine text and variables
# - Saving your work with Git
# -------------------------------------------

# Step 1: Variables Practice
# -----------------------------------------
# A variable stores information with a NAME and a VALUE.
# Example:
# fruit = "apple"
# colour = "red"
# print(f"The {fruit} is {colour}!")
#
# 👉 Good variable names describe what they store (fruit, colour).

# TODO:
# 1. Create three variables with values of your choice:
#    - favourite_sport (string)
#    - favourite_number (integer)
#    - favourite_food (string)
# 2. Print out 3 separate sentences using these variables with f-strings.
#    For example: "My favourite sport is football."
#    (Don’t just copy this! Use your own values.)

fave_sport = 'hockey'
fave_number = 101
fave_food = 'turkey'

print(f'I really enjoy watching {fave_sport}, especially with some {fave_food}!\nAlso i really like the number {fave_number}.')

# Step 2: Input Practice (ask the user for answers)
# -------------------------------------------------
# We can ask the user questions using input().
# Example:
# animal = input("What is your favourite animal? ")
#
# TODO:
# 1. Ask the user for their name
# 2. Store it in a variable called "name"
# 3. Print a message that says hello to them

name = input('Hello, what is your name?\n')

# Step 3: Combine Variables and Input
# -----------------------------------
# You can mix input variables with "pre-set" variables.
# Example:
# **Below is an input variable because we captured it from the user's input**
# city = input("What city do you live in? ")
# **Below is a "pre-set" variable because we manually gave it a value**
# current_year = 2025
# print(f"In {current_year}, you are living in {city}.")

# TODO:
# 1. Create a variable called current_year and set it to 2025
# 2. Ask the user for their age
# 3. Print a message showing their age and the current year

current_year = 2025
current_age = input('How old are you?\n')

print(f'The year is {current_year} and you are {current_age}!')


# -------------------------------------------
# Git Task: Submit your work!
# -------------------------------------------
# Once you have completed Steps 1–3, save your work with Git:
# 1. git add Ex0_revision.py
# 2. git commit -m "Completed main tasks"
# 3. git push origin main

# -------------------------------------------
# ⭐ Extension Challenges (Optional)
# -------------------------------------------
# If you finish the main tasks, try these extra challenges:

# Extension A:
# - Ask the user for their favourite drink and favourite place
# - Print a single, short message using name, drink, and place

# Extension B:
# - Also ask the user for their favourite hobby
# - Print a longer sentence combining year, age, and hobby
#   e.g. "In 2025, Sam is 20 years old and enjoys cycling."

# Extension C (Profile Card):
# - Create a "profile card" with at least 4 variables:
#    - name
#    - age
#    - favourite food
#    - favourite colour
# - Print them all neatly using \n, for example a profile card looks like this:
#    --- Profile ---
#    Name: ...
#    Age: ...
#    Food: ...
#    Colour: ...

# Extension D (Bonus Maths):
# - Ask the user for their age
# - Print how old they will be in 5 years
# - Print how many years until they are 100

# -------------------------------------------
# Git Task: Submit your work!
# -------------------------------------------
# Once you have completed any extensions, save your work again:
# 1. git add Ex0_revision.py
# 2. git commit -m "Completed extension tasks"
# 3. git push origin main
