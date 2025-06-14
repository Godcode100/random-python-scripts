Python 3.11.4 (main, Jul  5 2023, 14:15:25) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
def fibonacci_next(series=[1,1]):
    series.append(series[-1] + series[-2])
    return series

fib1 = fibonacci_next()
print(fib1)
[1, 1, 2]
fib1 = fibonacci_next()
print(fib1)
[1, 1, 2, 3]
fib2 = fibonacci_next(fib1)
print(fib2)
[1, 1, 2, 3, 5]
fib3 = fibonacci_next()
print(fib3)
[1, 1, 2, 3, 5, 8]
#In short, never use mutable values such as the list above for default argument values. Instead, use None as a default value.
#In the above example every function call creates an alias of the series list and mutates the series list further.
#By the time we try to call the function as at fib3 we cant get the original series list any more.
"""The proper way is to use None as a default argument value for mutable data types"""
'The proper way is to use None as a default argument value for mutable data types'
def fibon_next(series=None):
    if series is None:
        series = [1,1]
    return series.append(series[-1] + series[-2])

fib1 = fibon_next()
print(fib1)
None
fib10 = fibon_next(fib1)
print(fib10)
None
def fibons(series = None):
    if series is None:
        series = [1,1]
    series.append(series[-1] + series[-2])
    return series

fib1 = fibons()
print(fib1)
[1, 1, 2]
fib10 = fibons(fib1)
print(fib10)
[1, 1, 2, 3]
fib2 = fibons()
print(fib2)
[1, 1, 2]
print(fib1)
[1, 1, 2, 3]
print(fib10)
[1, 1, 2, 3]
print(fib2)
[1, 1, 2]


def roll_dice(sides=6,dice=1):
    return tuple(random.randint(1,sides) for _ in range(dice))

results, = roll_dice(dice=5,6)
SyntaxError: positional argument follows keyword argument
"""the above shows that always positional arg shd come before kwargs or any optional parameters"""
'the above shows that always positional arg shd come before kwargs or any optional parameters'
#the correct way of the functional call is:
results, = roll_dice(6,dice=7)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    results, = roll_dice(6,dice=7)
  File "<pyshell#44>", line 2, in roll_dice
    return tuple(random.randint(1,sides) for _ in range(dice))
  File "<pyshell#44>", line 2, in <genexpr>
    return tuple(random.randint(1,sides) for _ in range(dice))
NameError: name 'random' is not defined
import random
results, = roll_dice(6,dice=7)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    results, = roll_dice(6,dice=7)
ValueError: too many values to unpack (expected 1)
results1,results2,results3 = roll_dice(6,dice=3)
print(results1,results2,results3)
5 6 5

def roll_dices(sides=6,dice=1):
    return list(random.randint(1,sides) for _ in range(dice))

results = roll_dices(6,dice=7)
print(results)
[5, 1, 1, 2, 5, 3, 3]

"""VARIADIC PARAMETERS"""
'VARIADIC PARAMETERS'
#the opitional,required,and keyword arguments we have seen so far work when you know the number of arguments to be passed to a functional call
#meaning you are aware of how many parameters are in the function definition
#But what happens when you are not sure how many will be passed to a function. This is where arbitrary arguments lists or variadic parameters best operate
#Consider that we want to roll multiple dice but each die has different sides
#To represent variadic parameters use a single asteric followed by parameter name

def rollers(*dice):
    return tuple(random.randint(1,d) for d in dice)

results = rollers(11,4,5,6,7,8,9,2)
print(results)
(5, 2, 3, 2, 7, 3, 8, 1)
#we automatically pack multiple arguments into a single variadic parameter or variadic positional parameter,*dice, in this dice-rolling functional
#thereby allowing the rolling of multiple dice, where each die may have a different number of sides

"""using recursion instead of generator expression"""
'using recursion instead of generator expression'
>>> 
>>> def dices_roll(*dice):
...     if dice:
...         roll = random.randint(1,dice[0])
...         return (roll,) + dices_roll(*dice[1:])
...     return()
... 
>>> def rollo(*dices):
...     if dices:
...         roll = random.randint(1,*dices[0])
...         return (roll,) + rollo(*dices[1:])
...     return()
... 
>>> callable(rollo)
True
>>> callable(dices_roll)
True
>>> callable(results)
False
>>> callable(random)
False
>>> 
>>> """You can check whether an object is callable by passing it to the
... callable() function."""
'You can check whether an object is callable by passing it to the\ncallable() function.'
>>> help(callable)
Help on built-in function callable in module builtins:

callable(obj, /)
    Return whether the object is callable (i.e., some kind of function).
    
    Note that classes are callable, as are instances of classes with a
    __call__() method.

>>> """KEYWORD ARGUMENTS"""
'KEYWORD ARGUMENTS'
>>> #To capture an unknown number of keyword arguments, precede the
... #parameter name with two asterisks (**), making the parameter a keyword
... #variadic parameter. The keyword arguments passed to the function are
... #packed into a single dictionary object, so as to preserve the association
... #between keyword and value.
>>> 
>>> def call_something_else(func,*args,**kwargs):
...     return func(*args.**kwargs)
SyntaxError: invalid syntax
>>> 
>>> 
>>> def call_something_else(func,*args,**kwargs):
...     return func(*args,**kwargs)
... 
>>> #the call_something_else function doesnt need any knowledge of the func's parameter list instead any and every argument after thefirst positional argument
>>> #will get blindly passed on.
>>> def say_hi(name):
...     print(f"Hi,{name} glad to see you here. Praise God {name}")
... 
...     
>>> call_something_else(say_hi,name="Meshelemiah")
Hi,Meshelemiah glad to see you here. Praise God Meshelemiah
