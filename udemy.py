# from datetime import date
import math
# greet = 'heelllloooo'
# print(greet[0:len(greet)])

# print(greet.upper())
# print(greet.capitalize())
# print(greet.replace('heelllloooo', 'hello world!'))

# string are immutable: cann not change, overwrite, create or destroy. if you replace something it'll create a new string. Won't modify. Aka greet will stay but greet2 can be assigned a new str


# name = 'Waqar Habib'
# relationship_status = 'married'
# birth_year = input('when you born, dawg?')

# returns error
#age = 2022 - (birth_year)
#print(f'age:{age}')

# to solve, convert to integer
# age = 2022 - int(birth_year)
# print(f'age:{age}')

# to solve, can also do float (decimal point)
# age = 2022 - float(birth_year)
# print(f'age:{age}')

# fundamental data types
# int (number), float(decimal[floating pt #] ), str(string), bool(true/false), list, tuple, set, dict

# Other custom data types
#classes
#specialize = modules (extentsions)
#None (nothing) - idea of 0, absence of value

# int
# print(2+4)
# print(type(2+4))

# #float - takes more memory
# print(2/4)
# print(type(2/4))
# print(type(9.9+1.1))

# # math func
# print(round(3.1))
# print(round(3.9))

# #abs - absolute value (no negative #)
# print(abs(-20))

# #floor
# print(math.floor(3.1))

# excerise - password checker

# 1. ask for two input - user
# 2. another input - password
# 3. 
# 3. print password

# userName = input('username')
# password = input('password')

# password_length = len(password)
# hidden_password = '*'*password_length

# print(f"{userName}, your password is {hidden_password} is {password_length},")

# ******* lists *****


# amazon = ['notebooks','sunglasses','stapler','calculator']
# print(amazon[1])

# error: list index out of range = item doesnt exist in list

# list slicing

# # use ':' to print 0-2 entire list
# print(amazon[0:2])
# # use '::' to skip over items in list. skips sunglass
# print(amazon[0::2])

greet = 'hello'

# error:'str' object does not support item assignment
# means ln89 is immutable (can't be changed). Lists are mutable (or changeable)
#greet[0] = 'z'

# will be able to change, b/c mutable. 0 will be laptop
# amazon[0]= 'laptop'
# print(amazon)

# amazon = ['notebooks','sunglasses','stapler','calculator']

# amazon[0]= 'laptop'

# grab updated list. 
# print(amazon[0:3]) #slicing list creates new list
# print(amazon)

# amazon[0] = 'laptop'

# print entire old list

# print(amazon[0:3]) 

# below: old cart
amazon = ['notebooks','sunglasses','stapler','calculator']

# list slicing creates a copy 
# below: replace 'notebooks' in old cart w/ 'laptop
# amazon[0] = 'laptop'
# newCart = amazon[0:3]

# below new cart. replacing laptop with gum
# newCart[0] = 'gum'

# print both carts
# print (newCart)
# print (amazon)

# Q: what happens if amazon = newCart 
# A: modifies and makes both equal instead of slicing
# note: in var = newList[:] - ':' means copy of old list 

amazon[0] = 'laptop'

# IMP: create copy instead of modify
newCart = amazon[:]

# replace 'laptop' in old cart w/ 'gum'
amazon[0] = 'gum'

# print both
print (newCart)
print (amazon)

#***** revist list methods (sec 45/46) ****
#***** revist dictionary (sec 52) ****
#***** revist tuples (sec 52) ****
