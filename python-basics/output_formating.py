#Name : Bob Afwata
# Date : 11/02/2026
# Program to format the output in different styles

name = "Bob Afwata" #name

weight = 85 # weight in kgs 

fav_team = "Arsenal"

height = 126.86 # height in cms

# 1. Format using printf(f"{}")

print(f"My name is {name} and I weigh {weight} kgs.")

# 2 using f string 
msg = f"My name is {name} and I support {fav_team}"
print(msg)

#3  using {} and .format()

print("My name  {0} and I am {1} cms tall ".format(name,height))

# using output specifies %s -strings %f - float 0.123

import math
print('The value of pi is approximately %.3f.' % math.pi)
print("I support %s " %fav_team)