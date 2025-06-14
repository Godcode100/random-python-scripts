Python 3.11.4 (main, Jul  5 2023, 14:15:25) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
number is None
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    number is None
NameError: name 'number' is not defined
number = None
while number is None:
    if num == q:
        break
    elif:
        try:
            num = int(input("Enter a number"))
            number = num
        except ValueError:
            print("Enter a number")
        
    print(f"you entered {number}")
    
SyntaxError: invalid syntax

while number is None:
    if num == q:
        break
    else:
        try:
            num = int(input("Enter a number"))
            number = num
        except ValueError:
            print("Enter a number")

    print(f"you entered {number}")

    
Traceback (most recent call last):
  File "<pyshell#9>", line 2, in <module>
    if num == q:
NameError: name 'num' is not defined. Did you mean: 'sum'?
num
while number is None:
    if num == q:
        break
    else:
        try:
            num = int(input("Enter a number"))
            number = num
        except ValueError:
            print("Enter a number")

    print(f"you entered {number}")
    
SyntaxError: multiple statements found while compiling a single statement

num
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    num
NameError: name 'num' is not defined. Did you mean: 'sum'?
num
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    num
NameError: name 'num' is not defined. Did you mean: 'sum'?
number = None
while number is None:
    try:
        raw = input("Enter a number, or q to quit": )
        
SyntaxError: invalid syntax
while number is None:
    try:
        raw = input("Enter a number, or q to quit: " )
        if raw == 'q':
            break
        number = int(raw)
    except ValueError:
        print("You didnot enter a number")
print("You enetered {number}")
SyntaxError: invalid syntax
while number is None:
    try:
        raw = input("Enter a number, or q to quit: " )
        if raw == 'q':
            break
        number = int(raw)
    except ValueError:
        print("You didnot enter a number")
    print("You enetered {number}")

    
Enter a number, or q to quit: g
You didnot enter a number
You enetered {number}
Enter a number, or q to quit: 34
You enetered {number}
while number is None:
    try:
        raw = input("Enter a number, or q to quit: " )
        if raw == 'q':
            break
        number = int(raw)
    except ValueError:
        print("You didnot enter a number")
print(f"You enetered {number}")
SyntaxError: invalid syntax
print(f"You enetered {number}")while number is None:
    try:
        raw = input("Enter a number, or q to quit: " )
        if raw == 'q':
            break
        number = int(raw)
    except ValueError:
        print("You didnot enter a number")
else:
    print(f"You enetered {number}")
    
SyntaxError: invalid syntax
while number is None:
    try:
        raw = input("Enter a number, or q to quit: " )
        if raw == 'q':
            break
        number = int(raw)
    except ValueError:
        print("You didnot enter a number")
else:
    print(f"You enetered {number}")

    
You enetered 34

while number is None:
    try:
        raw = input("Enter a number, or q to quit: " )
        if raw == 'q':
            break
        number = int(raw)
    except ValueError:
        print("You didnot enter a number")
else:
    print(f"You enetered {number}")

    
You enetered 34
help(collection)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    help(collection)
NameError: name 'collection' is not defined
import collection
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    import collection
ModuleNotFoundError: No module named 'collection'
help(list)

help(deque)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    help(deque)
NameError: name 'deque' is not defined
import deque
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    import deque
ModuleNotFoundError: No module named 'deque'
help(tuple)

help(set)

import collections
help(collections)

help(deque)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    help(deque)
NameError: name 'deque' is not defined
from collections import deque
help(deque)

from collections import namedtuple
help(namedtuple)
Help on function namedtuple in module collections:

namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
    Returns a new subclass of tuple with named fields.
    
    >>> Point = namedtuple('Point', ['x', 'y'])
    >>> Point.__doc__                   # docstring for the new class
    'Point(x, y)'
    >>> p = Point(11, y=22)             # instantiate with positional args or keywords
    >>> p[0] + p[1]                     # indexable like a plain tuple
    33
    >>> x, y = p                        # unpack like a regular tuple
    >>> x, y
    (11, 22)
    >>> p.x + p.y                       # fields also accessible by name
    33
    >>> d = p._asdict()                 # convert to a dictionary
    >>> d['x']
    11
    >>> Point(**d)                      # convert from a dictionary
    Point(x=11, y=22)
    >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
    Point(x=100, y=22)

coffeeOrder = namedtuple("coffeeOrder",('item','addon','to_go'))
>>> order = coffeeOrder("pumpkin latte",("whipped cream",),True)
>>> print(order[1],order[2],order[3])
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    print(order[1],order[2],order[3])
IndexError: tuple index out of range
>>> print(order[0],order[1],order[2])
pumpkin latte ('whipped cream',) True
>>> print(order.index)
<built-in method index of coffeeOrder object at 0x7f901c5ccc20>
>>> print(order.count)
<built-in method count of coffeeOrder object at 0x7f901c5ccc20>
>>> print(order.addon)
('whipped cream',)
>>> materials = namedtuple("Builder",("hardware","cost"))
>>> site = materials("Tororo Cement",15000)
>>> site[1]
15000
>>> site[0]
'Tororo Cement'
>>> import array
>>> help(array)

>>> raffle = {"james","simon","denis"}
>>> raffle.add("hanna")
>>> print(raffle)
{'denis', 'simon', 'hanna', 'james'}
>>> raffle.pop("clement")
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    raffle.pop("clement")
TypeError: set.pop() takes no arguments (1 given)
>>> raffle.discard("clement")
>>> raffle.pop()
'denis'
>>> print(raffle)
{'simon', 'hanna', 'james'}
