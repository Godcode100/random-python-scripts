Python 3.11.4 (main, Jul  5 2023, 14:15:25) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
"""Structural pattern matching which was introduced in python 3.10 supports matching objects in patterns by their attributes"""
'Structural pattern matching which was introduced in python 3.10 supports matching objects in patterns by their attributes'
"""I might have a class that represents a pizza and i might want to perform structural pattern matching based on attributes in a given Pizza Object"""
'I might have a class that represents a pizza and i might want to perform structural pattern matching based on attributes in a given Pizza Object'
class Pizza:
    def __init__(self,topping,second_topping=None):
        self.first = topping
        self.second = second_topping

        
order = Pizza("Pepperoni","mushrooms")
match order:
    case Pizza(first="Pepperoni",second="mushrooms")
    
SyntaxError: incomplete input
match order:
    case Pizza(first="Pepperoni",second="mushrooms")
    
SyntaxError: incomplete input
match order:
    case Pizza(first="Pepperoni",second="mushrooms"):
        print("Ansi standard pizza")
    case Pizza(first="pineapple")
    
SyntaxError: incomplete input
match order:
    case Pizza(first="Pepperoni",second="mushrooms"):
        print("Ansi standard pizza")
    case Pizza(first="pineapple"):
        print("Is this even pizza?")
    case Pizza(first=first,second='cheese'):
        print(f"Very cheesy pizza with {first}")
    case Pizza(first=first,second=second):
        print(f"Pizza with {first} and {second}")

        
Ansi standard pizza
order= Pizza("cucumber")match order:
    case Pizza(first="Pepperoni",second="mushrooms"):
        print("Ansi standard pizza")
    case Pizza(first="pineapple"):
        print("Is this even pizza?")
    case Pizza(first=first,second='cheese'):
        print(f"Very cheesy pizza with {first}")
    case Pizza(first=first,second=second):
        print(f"Pizza with {first} and {second}")
        
SyntaxError: invalid syntax
order= Pizza("cucumber")
match order:
    case Pizza(first="Pepperoni",second="mushrooms"):
        print("Ansi standard pizza")
    case Pizza(first="pineapple"):
        print("Is this even pizza?")
    case Pizza(first=first,second='cheese'):
        print(f"Very cheesy pizza with {first}")
    case Pizza(first=first,second=second):
        print(f"Pizza with {first} and {second}")

        
Pizza with cucumber and None
"""The above works well if you dont mind typing out the attributes however may feel redundant if you have to write out the attributes each time.A case in point is if you have a Point class that represents apoint in three dimensional space. it may feel tedious to spell out x,y,z each time"""
'The above works well if you dont mind typing out the attributes however may feel redundant if you have to write out the attributes each time.A case in point is if you have a Point class that represents apoint in three dimensional space. it may feel tedious to spell out x,y,z each time'
class Point:
    def __init__(self,x,y,z):
        self.x_pos = x
        self.y_pos = y
        self.z_pos = z

        
Point(0,100,0)
<__main__.Point object at 0x7fca6fd25110>
point = Point(0,100,0)
match point:
    case Point(x_pos =0,y_pos=0,z_pos=0)
    
SyntaxError: incomplete input
match point:
    case Point(x_pos =0,y_pos=0,z_pos=0):
        print("You are here")
        case Point(x_pos =0,y_pos=_,z_pos=0):
            
SyntaxError: invalid syntax
match point:
    case Point(x_pos =0,y_pos=0,z_pos=0):
        print("You are here")
    case Point(x_pos =0,y_pos=_,z_pos=0):
        print("Look Up")

        
Look Up
"""The above pattern feels pretty long especially when people would expect to specify a point in 3D as x,y,z"""
'The above pattern feels pretty long especially when people would expect to specify a point in 3D as x,y,z'
"""Instead of writing out the attributes each time i could specify the special __match_args__  class attribute to specify how a pattern's values match postionally to the object's attributes"""
"Instead of writing out the attributes each time i could specify the special __match_args__  class attribute to specify how a pattern's values match postionally to the object's attributes"
class Point:
    __match_args__ =('x_pos','y_pos','z_pos')
    def __init__(self,x,y,z):
        self.x_pos = x
        self.y_pos = y
        self.x_pos = z

        
point = Point(0,123,0)
match point:
    case Point(0,0,0):
        print("You are here")
    case(0,_,0):
        print("We only look to God")

        
match point:
    case Point(0,0,0):
        print("You are here")
    case Point(0,_,0):
        print("We only look to God")

        
class Point:
    __match_args__ =('x_pos','y_pos','z_pos')
    def __init__(self,x,y,z):
        self.x_pos = x
...         self.y_pos = y
...         self.z_pos = z
... 
...         
>>> point = Point(0,123,0)
>>> match point:
...     case Point(0,0,0):
...         print("You are here")
...     case Point(0,_,0):
...         print("We only look to God")
... 
...         
We only look to God
>>> """We define __match_args__ as a tuple of strings represnting the attributes we want to map to positionalvalues in pattern matching on the object"""
'We define __match_args__ as a tuple of strings represnting the attributes we want to map to positionalvalues in pattern matching on the object'
>>> 
>>> 
>>> """Unlike class centric languages like java and c\# an important part in python programming is knowing when to use classes and when not to use classes"""
'Unlike class centric languages like java and c\\# an important part in python programming is knowing when to use classes and when not to use classes'
>>> 
>>> 
>>> """
... You shouldnt use a class where a module would be sufficient.Python modules allow you to organise variables and functions by ourpose or category so you dont need to use the classes in the same manner
... """
'\nYou shouldnt use a class where a module would be sufficient.Python modules allow you to organise variables and functions by ourpose or category so you dont need to use the classes in the same manner\n'
>>> 
>>> 
>>> """The purpose of a class is to bundle data with the methods responsible for accessing and modifying that data"""
'The purpose of a class is to bundle data with the methods responsible for accessing and modifying that data'
