""" My First Python script """

__version__ = "3"
__author__ = "@rasta0981 - Darren K."

import var

name = input(var.nametext)
age = int(input(var.agetext))
new_age = age + 1
birth_year = 2025-new_age
new_name = name.upper()
print(f"Hello {new_name}\nYour age is {new_age}\nYou were born {birth_year}")
