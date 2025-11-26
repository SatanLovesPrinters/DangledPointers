# https://programming-25.mooc.fi/part-1

# getting started

print (":-)")

greeting = "Hello there!"

# minutes in a year 
minutes = 60
hours_in_day = 24
days_in_year = 365

minutes_in_day = minutes * hours_in_day
minutes_in_year = minutes_in_day * days_in_year

print (f"{greeting}")
print (f"Minutes in 1 day: {minutes_in_day}")
print(f"Minutes in 1 year: {minutes_in_year}")

# intro to input

input_name = input("What is your name?: ")
input_email = input("What is your email address?: ")
input_nickname = input("What is your nickname?: ")

print("Let's confirm the details!")
print(f"Your name: {input_name}")
print(f"Your email address: {input_email}")
print(f"Your nickname: {input_nickname}")

input_name = input("What is your name again?: ")
print(f"Ah right! Your name is: {input_name}")

# Story Example

story_name = input("What is the story-be-tolder's name?: ")
story_year = input("What year does this story take place?: ")
story_general = input("Explain the story!: ")
story_complete = print(f"The story begins with {story_name} on a warm day in the year {story_year}. {story_general}")

# more about variables (str, int, float)