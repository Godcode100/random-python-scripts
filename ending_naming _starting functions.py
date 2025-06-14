Python 3.11.4 (main, Jul  5 2023, 14:15:25) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
board = [["-"] *3]*3
print(board)
[['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
board[1][0] = "X"
print(board)
[['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]
boxes = [["Q"]*3\n]3
SyntaxError: unexpected character after line continuation character
boxes = [["Q"]*3\n]*3
SyntaxError: unexpected character after line continuation character
boxes = [["Q"]*3]\n*3
SyntaxError: unexpected character after line continuation character
#print board to screen
for row in board:
    print(f"{row[0]} {row[1]} {row[2]}")

    
X - -
X - -
X - -
manga = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
manga[1][0] = 'O'
print(manga)
[['-', '-', '-'], ['O', '-', '-'], ['-', '-', '-']]
#whenever you’re working with a collection, remember that an item is no different from any other name.
#Immutability exists mainly for efficiency, not for protecting data.
class Taco:
    def __init__(self):
        self.ingredients=toppings

        
class Taco:
    def __init__(self):
        self.ingredients=toppings
    def add_sauce(self,sauce)
    
SyntaxError: incomplete input
class Taco:
    def __init__(self):
        self.ingredients=toppings

        
class Taco:
    def __init__(self):
        self.ingredients=toppings
    def add_sauce(self,sauce):
        
SyntaxError: invalid syntax
class Taco:
    def __init__(self,toppings):
        self.ingredients=toppings
        
    def add_sauce(self,sauce):
        self.ingredients.append(sauce)

        
def Pizza:
    
SyntaxError: incomplete input
class Pizza:
    def __init__(self,toppings):
        self.ingredients = toppings

    
class Pizza:
    def __init__(self,toppings):
        self.ingredients = toppings
        
    def add_spice(self,spice):
        self.ingredients.append(spice)

        
ingredients = ["Tomatoes","lettuce"]
chicken = Pizza.ingredients()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    chicken = Pizza.ingredients()
AttributeError: type object 'Pizza' has no attribute 'ingredients'
chicken = Pizza.toppings()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    chicken = Pizza.toppings()
AttributeError: type object 'Pizza' has no attribute 'toppings'
chicken = Pizza()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    chicken = Pizza()
TypeError: Pizza.__init__() missing 1 required positional argument: 'toppings'
class Pizza:
    def __init__(self,toppings):
        ingredients = toppings

    
class Pizza:
    def __init__(self,toppings):
        self.ingredients = toppings
        
    def add_spice(self,spice):
        self.ingredients.append(spice)
        
SyntaxError: invalid syntax
    
class Pizza:
    def __init__(self,toppings):
        ingredients = toppings
        
    def add_spice(self,spice):
        self.ingredients.append(spice)

chicken = Pizza(ingredients)
veges = Pizza.ingredients
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    veges = Pizza.ingredients
AttributeError: type object 'Pizza' has no attribute 'ingredients'
print(chicken)
<__main__.Pizza object at 0x7f81ee06ffd0>
ingredients = ["Tomatoes","lettuce"]
chicken = Pizza(ingredients)
print(chicken)
<__main__.Pizza object at 0x7f81eec38450>
print(chicken.ingredients)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print(chicken.ingredients)
AttributeError: 'Pizza' object has no attribute 'ingredients'
default_toppings = ["Lettuce", "Tomato", "Beef"]
chickens = Pizza(default_toppings)
print(chickens.ingredients)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    print(chickens.ingredients)
AttributeError: 'Pizza' object has no attribute 'ingredients'
print(chickens.toppings)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    print(chickens.toppings)
AttributeError: 'Pizza' object has no attribute 'toppings'
print(chickens.default_toppings)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print(chickens.default_toppings)
AttributeError: 'Pizza' object has no attribute 'default_toppings'
class Pizza:
    def __init__(self,toppings):
        self.ingredients = toppings
        
    def add_spice(self,spice):
        self.ingredients.append(spice)

        
default_toppings = ["Lettuce", "Tomato", "Beef"]
chickens = Pizza(default_toppings)
SyntaxError: multiple statements found while compiling a single statement
default_toppings = ["Lettuce", "Tomato", "Beef"]
chickens = Pizza(default_toppings)
print(chickens.ingredients)
['Lettuce', 'Tomato', 'Beef']
marine = Pizza(default_toppings)
marine.add_spice("veges")
print(marine)
<__main__.Pizza object at 0x7f81eed413d0>
print(marine.ingredients)
['Lettuce', 'Tomato', 'Beef', 'veges']
print(chickens.ingredients)
['Lettuce', 'Tomato', 'Beef', 'veges']
print(marine)
<__main__.Pizza object at 0x7f81eed413d0>
print(chickens)
<__main__.Pizza object at 0x7f81ef458150>
id(chickens)
140196041818448
id(marine)
140196034384848
id(marine.ingredients)
140196020915392
id(chickens.ingredients)
140196020915392
id(default_toppings)
140196020915392
import copy
h
help(copy)

class Taco:
    def__init__(self,toppings):
        
SyntaxError: incomplete input
class Taco:
    def __init__(self,toppings):
        self.ingredients = copy.copy(toppings)
    def add_sauce(self,sauce):
        self.ingredients.add_sauce(sauce)

        
default_tops=["cheese","bacon"]
mild_taco = Taco(default_tops)
print(mild_taco)
<__main__.Taco object at 0x7f81ef5f1fd0>
print(mild_taco.ingredients)
['cheese', 'bacon']
wild_taco = copy.deepcopy(mild_taco)
print(wild_taco.ingredients)
['cheese', 'bacon']
wild_taco.add_sauce("Chicken Masala")
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    wild_taco.add_sauce("Chicken Masala")
  File "<pyshell#80>", line 5, in add_sauce
    self.ingredients.add_sauce(sauce)
AttributeError: 'list' object has no attribute 'add_sauce'
wild_taco.ingredients.add_sauce("chicken masala")
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    wild_taco.ingredients.add_sauce("chicken masala")
AttributeError: 'list' object has no attribute 'add_sauce'
wild_taco.add_sauce("chicken")
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    wild_taco.add_sauce("chicken")
  File "<pyshell#80>", line 5, in add_sauce
    self.ingredients.add_sauce(sauce)
AttributeError: 'list' object has no attribute 'add_sauce'
class Taco:
    def __init__(self,toppings):
        self.ingredients = toppings
    def add_sauce(self,sauce):
        self.ingredients.append(sauce)

        
default_tops=["cheese","bacon"]


mild_taco = Taco(default_tops)
wild_taco =copy.deepcopy(mild_taco)
wild_taco.add_sauce("Chicken Masala")
print(mild_taco,wild_taco)
<__main__.Taco object at 0x7f81ee078510> <__main__.Taco object at 0x7f81ee076590>
print(mild_taco.ingredients,wild_taco.ingredients)
['cheese', 'bacon'] ['cheese', 'bacon', 'Chicken Masala']


"""Functional programming Paradigm """
'Functional programming Paradigm '
#A functional to simulate rolling a die
import random
def roll_dice(sides):
    return random.randint(1,sides)
roll_dice(6)
SyntaxError: invalid syntax
roll = roll_dice(6)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    roll = roll_dice(6)
NameError: name 'roll_dice' is not defined
roll_dice(6)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    roll_dice(6)
NameError: name 'roll_dice' is not defined
def roll_dice(sides):
    return random.randint(1,sides)

roll = roll_dice(6)
roll
4

#Multiple dice
def many_dice(sides,dice):
    return tuple(random.randint(1,sides) for _ in range(dice))

player1 = many_dice(6,3)
player
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    player
NameError: name 'player' is not defined. Did you mean: 'player1'?
player1
(5, 3, 5)
player1[2]
5
player2,player3 = many_dice(6,2)
player2,player3
(6, 3)
player3
3
player2
6
player2,player3 = many_dice(6,3)
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    player2,player3 = many_dice(6,3)
ValueError: too many values to unpack (expected 2)
player2= many_dice(6,2)
player2
(5, 6)
player2,player3 = many_dice(6,1)
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    player2,player3 = many_dice(6,1)
ValueError: not enough values to unpack (expected 2, got 1)
player3 = many_dice(6,1)
player3
(3,)
player2,player3 = many_dice(6,3)
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    player2,player3 = many_dice(6,3)
ValueError: too many values to unpack (expected 2)
player2,player3 = many_dice(6,2)
player2
6
player3
4
player2,player3
(6, 4)

#the above used a generator where by we are having a random generated number for every dice and unpacking it into a tuple

"""Using a recursive Function instead of a tuple """
'Using a recursive Function instead of a tuple '

def dice(sides,dice):
    if dice < 1:
        return ()
    roll = random.randint(1,sides)
    return (roll,) + dice(sides,dice-1)

dice(6,3)
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    dice(6,3)
  File "<pyshell#150>", line 5, in dice
    return (roll,) + dice(sides,dice-1)
TypeError: 'int' object is not callable
>>> turn = dice(6,3)
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    turn = dice(6,3)
  File "<pyshell#150>", line 5, in dice
    return (roll,) + dice(sides,dice-1)
TypeError: 'int' object is not callable
>>> def dice(sides,dices):
...     if dices < 1:
...         return ()
...     roll = random.randint(1,sides)
...     return (roll,) + dice(sides,dices-1)
... 
>>> turn = dice(6,3)
>>> turn
(2, 6, 2)
>>> print(turn)
(2, 6, 2)
>>> dice_cup = dice(6,5)
>>> print(dice_cup)
(2, 3, 6, 1, 1)
>>> print(dice_cup)
(2, 3, 6, 1, 1)
>>> for x in dice_cup:
...     print(x)
... 
...     
2
3
6
1
1
>>> dice(6,5) for x in range(5):
...     
SyntaxError: invalid syntax
>>> print(dice(6,5))
(4, 1, 3, 3, 1)
>>> print(dice(6,5) for x in range (6))
<generator object <genexpr> at 0x7f81ef2d7680>
>>> 
>>> import sys
>>> help(sys)

>>> sys.last_type()
TypeError()
>>> sys.audit(dice(6,5))
>>> def dicer(sides,dices):
...     if dices < 1:
...         return()
...     roll = random.randint(1,sides)
