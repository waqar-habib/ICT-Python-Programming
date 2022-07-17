#  OOP - Object Oriented Programming

# Everything is an object - divide the big functionality/data into multiple pieces by creating custom objects (classes) and then combine them into a single object)

'''
class PlayerCharacter:
   def __init__(self, name):
       self.name = name
    
def run(self):
    print('run')
    
player1 = PlayerCharacter()

print(player1)

# run the above and error:
# PlayerCharacter.__init__() missing 1 required positional argument: 'name'--- b/c init is a special method (dunder/magic method). When building a class, this is a constructor and is auto called when we instantiate the class (call the object). runs init, but no args were given. When calling init, accept a positional argument (whatever is after self as the parameter)

'''
# to solve, give parameter a name, pass it when instantiating the method
class PlayerCharacter:
   def __init__(self, name, age):
       self.name = name #attribute
       self.age = age #attribute
    
def run(self):
    print('run')

# passing name PARAMETER from ln 23
# pass another PARAM
player1 = PlayerCharacter('Meelyi', 16)
player2 = PlayerCharacter('Tom', 15)

# run the above..shows player char @ what position. 
# print(player1)

# what is self and what is ln23? "self" is a way to define the PlayerCharacter class. Self.name = param

# prints the param  --> Meeyi
print(player1.name) # meelyi
print(player2.name) # tom 

# Object NEEDS to have an ATTRIBUTE. in ln24 "name" is an attribute. "self" (to the left of the attribute is a REFERENCE).

# objects make code dynamic by allowing you to substitute different PARAMS while using same object code. 

# prints name and age since two params are passed

print(f"'Name:' {player1.name}, 'Age: {player1.age}") # meelyi
print(f"'Name:' {player2.name}, 'Age: {player2.age}") # meelyi