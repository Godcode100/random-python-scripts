Python 3.11.4 (main, Jul  5 2023, 14:15:25) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
"""WHY LAMBDAS ARE USEFUL"""
'WHY LAMBDAS ARE USEFUL'

#Many programmers cant imagine ever needing a nameles or anaonymous functions
#The code represents a player character in a text adventure game

import random
health = 10
xp = 10

def attempt(action,min_roll,outcome):
    global health,xp
    roll = random.randint(1,20)
    if roll >= min_roll:
        print(f"{action} SUCCEDED")
        result = True

        
def attempt(action,min_roll,outcome):
    global health,xp
    roll = random.randint(1,20)
    if roll >= min_roll:
        print(f"{action} SUCCEDED")
        result =True

        
def attempt(action,min_roll,outcome):
    global health,xp
    roll = random.randint(1,20)
    if roll >= min_roll:
        print(f"{action} SUCCEDED")
        result =True
    else:
        print(f"{action} FAILED")
        result = False

    
def attempt(action,min_roll,outcome):
    global health,xp
    roll = random.randint(1,20)
    if roll >= min_roll:
        print(f"{action} SUCCEDED")
        result =True
    else:
        print(f"{action} FAILED")
        result = False
    scores = outcome(result)
    health = health + scores[0]
    print(f"Health is now {health}")
    xp = xp + scores[1]
    print(f"xp is now {xp}")
    return result

def eat_bread(success):
    if success:
        return(1,0)
    return (-1,0)
def fight_ice(success):
    
SyntaxError: invalid syntax
def eat_bread(success):
    if success:
        return(1,0)
    return (-1,0)

def fight_in_ice(success):
    if success:
        return(10,10)
    return(0,10)

attempt("Eating bread",5,eat_bread)
Eating bread SUCCEDED
Health is now 11
xp is now 10
True
attempt("Eating bread",5,eat_bread)
Eating bread SUCCEDED
Health is now 12
xp is now 10
True
attempt("Eating bread",5,eat_bread)
Eating bread SUCCEDED
Health is now 13
xp is now 10
True
attempt("Eating bread",5,eat_bread)
Eating bread SUCCEDED
Health is now 14
xp is now 10
True
attempt("Eating bread",5,eat_bread)
Eating bread SUCCEDED
Health is now 15
xp is now 10
True
attempt("Eating bread",5,eat_bread)
Eating bread SUCCEDED
Health is now 16
xp is now 10
True
attempt("Eating bread",5,eat_bread)
Eating bread SUCCEDED
Health is now 17
xp is now 10
True
attempt("Eating bread",5,eat_bread)
Eating bread SUCCEDED
Health is now 18
xp is now 10
True
attempt("Eating bread",5,eat_bread)
Eating bread SUCCEDED
Health is now 19
xp is now 10
True
attempt("Eating bread",5,eat_bread)
Eating bread FAILED
Health is now 18
xp is now 10
False
attempt("Eating bread",5,eat_bread)
Eating bread SUCCEDED
Health is now 19
xp is now 10
True
attempt("Eating bread",5,eat_bread)
Eating bread SUCCEDED
Health is now 20
xp is now 10
True
attempt("Eating bread",5,eat_bread)
Eating bread SUCCEDED
Health is now 21
xp is now 10
True
attempt("Eating bread",5,eat_bread)
Eating bread SUCCEDED
Health is now 22
xp is now 10
True
attempt("Eating bread",5,eat_bread)
Eating bread SUCCEDED
Health is now 23
xp is now 10
True
attempt("Eating bread",5,eat_bread)
Eating bread FAILED
Health is now 22
xp is now 10
False


attempt("Fighting ice",5,fight_in_ice)
Fighting ice SUCCEDED
Health is now 32
xp is now 20
True

attempt("Fighting ice",5,fight_in_ice)
Fighting ice SUCCEDED
Health is now 42
xp is now 30
True

attempt("Fighting ice",5,fight_in_ice)
Fighting ice SUCCEDED
Health is now 52
xp is now 40
True

attempt("Fighting ice",5,fight_in_ice)
Fighting ice SUCCEDED
Health is now 62
xp is now 50
True

attempt("Fighting ice",5,fight_in_ice)
Fighting ice SUCCEDED
Health is now 72
xp is now 60
True

attempt("Fighting ice",5,fight_in_ice)
Fighting ice SUCCEDED
Health is now 82
xp is now 70
True

attempt("Fighting ice",5,fight_in_ice)
Fighting ice SUCCEDED
Health is now 92
xp is now 80
True
attempt("Fighting ice",5,fight_in_ice)
Fighting ice FAILED
Health is now 92
xp is now 90
False
#In such a situation we could implement lambdas as below
#Take an example of another action suchas high glide where success increases health by 2 and xp by 4
#else health is cut by -5 and xp is increased by 2

attempt("High gliding", 8,high_glide(success):(2,4) if success else(-5,2))
SyntaxError: invalid syntax
attempt("High Gliding",8,lambda(success):(2,4) if success else(-5,2))
SyntaxError: Lambda expression parameters cannot be parenthesized
attempt("High gliding",8,lambda success :(2,4) if success else (-5,2))
High gliding SUCCEDED
Health is now 94
xp is now 94
True

attempt("High gliding",8,lambda success :(2,4) if success else (-5,2))
High gliding FAILED
Health is now 89
xp is now 96
False

attempt("High gliding",8,lambda success :(2,4) if success else (-5,2))
High gliding SUCCEDED
Health is now 91
xp is now 100
True

attempt("High gliding",8,lambda success :(2,4) if success else (-5,2))
High gliding SUCCEDED
Health is now 93
xp is now 104
True

attempt("High gliding",8,lambda success :(2,4) if success else (-5,2))
High gliding SUCCEDED
Health is now 95
xp is now 108
True

"""LAMBDAS AS SORTING KEYS"""
'LAMBDAS AS SORTING KEYS'
#One of the most common situations where lambdas come in handy is when specifying a key function
#A key function is a callable that returns a part of a function that should be used for sorting.
#A key function is passed to another function that is reponsible for sorting data in some way.
'''A key function is a callable that returns the part of a collection or object that should be used for sorting.'''
'A key function is a callable that returns the part of a collection or object that should be used for sorting.'
#Below is people which is a list of tuples
people = [
    ("Joe","Hacks"),
    ("Jesus", "Christ"),
    ("God","The Father").
    ("Holy","Spirit")
    
SyntaxError: '[' was never closed
people = [
    ("Joe","Hacks"),
    ("Jesus", "Christ"),
    ("God","The Father").
    ("Holy","Spirit")]
    
SyntaxError: invalid syntax
people = [
    ("Joe","Hacks"),
    ("Jesus", "Christ"),
    ("God","The Father").
    ("Holy","Spirit")]
    
SyntaxError: invalid syntax
people = [
    ("Joe","Hacks"),
    ("Jesus", "Christ"),
    ("God","The Father"),
    ("Holy","Spirit")]
    
#we now want to sort our list of tuples by last_name and remember list object has a sorted function for sorting list
    
#Here we ant to sort by last name and sorted has a key argument that takes a function or other callable
    
by_last_name = sorted(people,key=lambda x:x[1])
    
print(by_last_name)
    
[('Jesus', 'Christ'), ('Joe', 'Hacks'), ('Holy', 'Spirit'), ('God', 'The Father')]
#Remember lists are mutable so using sorted helps us create new list
    
"""The sorted function uses the key argument ,which is always a function or callable ,by passing a each item to it 
and then using then using the value returned from that callable to determine the sorting order. Since i want the
tuples sorted by last name,which is the second item of the tuple i have the lambdas return that item which is x[1]"""
    
'The sorted function uses the key argument ,which is always a function or callable ,by passing a each item to it \nand then using then using the value returned from that callable to determine the sorting order. Since i want the\ntuples sorted by last name,which is the second item of the tuple i have the lambdas return that item which is x[1]'



'''DECORATORS'''
    
'DECORATORS'
'''Decorators allow you to modify the behaviour of a function or multiple functions by wrapping it in an additional layer of logic.'''
    
'Decorators allow you to modify the behaviour of a function or multiple functions by wrapping it in an additional layer of logic.'
#This changes the behaviour of a function without you having to rewrite the function itself.
    
#Lets first use an example where decorators are not used.
    
character = "Sir Bob"
    
health = 15
    
xp = 0
    
def eat_food(food):
    global health
    if health <= 0:
        print(f'{character} is too weak')
        return
    print(f'{character} ate {food}')
    health += 1
    print(f" Health:{health} | XP: {xp}")

    
def fight_monster(monster,strength):
    global health,xp
    if health <= 0:
        print(f"{character} is too weak")
        return
    if random.randint(1,20) >= strength:
        print(f"{character} defeated {monster}")
        xp += 10
    else:
        print(f'{character} flees {monster}')
        health -=10
        xp +=5
    print(f" Health:{health} | XP:{xp}")

    
eat_food("chappati")
Sir Bob ate chappati
 Health:16 | XP: 0
fight_monster("vamp",15)
Sir Bob defeated vamp
 Health:16 | XP:10
fight_monster("vamp",15)
Sir Bob flees vamp
 Health:6 | XP:15
fight_monster("vamp",15)
Sir Bob flees vamp
 Health:-4 | XP:20
eat_food("Chappati")
Sir Bob is too weak
fight_monster("Lion",1)
Sir Bob is too weak
"""Each function represents an action a player can take and some code is shared between the 2 functions.
1St and foremost we check the health of a charcter and if it is less or equal zero the character cannot
perform any action instead we just print the charcter is too weak and exit. The stats of a character
are only displayed when an action is completed"""
'Each function represents an action a player can take and some code is shared between the 2 functions.\n1St and foremost we check the health of a charcter and if it is less or equal zero the character cannot\nperform any action instead we just print the charcter is too weak and exit. The stats of a character\nare only displayed when an action is completed'


"""APPLYING DECORATORS"""
'APPLYING DECORATORS'
#The repaeated code is not very pythonic.The first instinct is to move out the common code, that checks the health first and the one that displays character stats,into their
#own functions.However you still need to call each one within every character action function
#Further more each function would still require that conditional statement to ensure code isnt run when health is too low.

"""This kind of situation where i want to run the same code before and after every function can perfectly be solved by decorators"""
'This kind of situation where i want to run the same code before and after every function can perfectly be solved by decorators'


import functools
character = "Sir Bob"
health = 15
xp = 10

def character_action(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        global health,xp
        if health <= 0:
            print(f"{character} is too weak")
            return
        result = func(*args,**kwargs)
        print(f" Health:{health} | XP:{health}")
        return result
    return wrapper

#Adecorator is most often implemented as a closure which closes over a function or any other callable object being modified
#The decoarator itself,caharcter_action accepts a func parameter which is the callable being modified.
#Within the decorator is the wrapper which is the callable oject where the decorator's logic lives.
#Bse i dont know how many arguments will be passed to the function i apply the decorator to, I set up the wrapper to accept variadic arguments
#the @functools.wraps(func) line prevents the callable object being wrapped from having its identity concealed from the rest of the program.
#without that line wrapping the callable would mess the external access of important function attributes such as __doc__(the doc string) and __name__
#This line is itseldf a decorator that ensures all important attributes of the callable are retained bby the now wrapped function thus making all important attributes
#accessible outside the function in all usual ways.
#Inside the wrapper i put all the logic i want to run before and after each function.
#After checking health i call the function that is bound to func unpacking all variadic arguments into the call and bind the returned value to result.
#in this way i can ensure that gets returned from the decorator after i print the stats
#in this way i can ensure that gets returned from the decorator after i print the stats

"""TYPE HINTING AND FUNCTION ANNOTATIONS"""
'TYPE HINTING AND FUNCTION ANNOTATIONS'

===================================================================== RESTART: /home/joelouma/Desktop/type_hinting.py =====================================================================
<generator object roll_dice.<locals>.<genexpr> at 0x7effb52cd3f0>

>>> answer:int=6
>>> print(answer)
6
>>> print(str(answer))
6
>>> 
===================================================================== RESTART: /home/joelouma/Desktop/type_hinting.py =====================================================================
<generator object roll_dice.<locals>.<genexpr> at 0x7f9b8959d3f0>
Help on _SpecialForm in module typing:

Optional = typing.Optional
    Optional[X] is equivalent to Union[X, None].

>>> import typing
>>> 
===================================================================== RESTART: /home/joelouma/Desktop/type_hinting.py =====================================================================
<generator object roll_dice.<locals>.<genexpr> at 0x7f9e6ba293f0>
Help on _SpecialForm in module typing:

Optional = typing.Optional
    Optional[X] is equivalent to Union[X, None].

{'sides': <class 'int'>, 'dice': <class 'int'>, 'return': typing.Tuple[int, ...]}
>>> help(typing.Any)
Help on class Any in module typing:

class Any(builtins.object)
 |  Any(*args, **kwargs)
 |  
 |  Special type indicating an unconstrained type.
 |  
 |  - Any is compatible with every type.
 |  - Any assumed to have all methods.
 |  - All values assumed to be instances of Any.
 |  
 |  Note that all the above statements are true from the point of view of
 |  static type checkers. At runtime, Any should not be used with instance
 |  checks.
 |  
 |  Static methods defined here:
 |  
 |  __new__(cls, *args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

>>> help(typing.Iterable)
Help on _SpecialGenericAlias in module typing:

Iterable = typing.Iterable
    A generic version of collections.abc.Iterable.

