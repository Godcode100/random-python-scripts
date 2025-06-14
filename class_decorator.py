Python 3.11.4 (main, Jul  5 2023, 14:15:25) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
import functools
def charcter_action(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        global health
        if health <= 0:
            print(f"{charcter} is too weak")
            return
        result = func(*args,**kwargs)
        print(f'Health:{health} | XP:{xp}')
        return result
    return wrapper
# the above are decorators in functions

"CLASS DECORATORS"
'CLASS DECORATORS'
"""Classes support decoartors much like functions do"""
'Classes support decoartors much like functions do'
"""class decorators wrap the instantiation of a class allowing you to intervene in any number of ways:adding attributes,intializing another class containing an instance of the one being decorated or performing some behavior immediately on the new object"""
'class decorators wrap the instantiation of a class allowing you to intervene in any number of ways:adding attributes,intializing another class containing an instance of the one being decorated or performing some behavior immediately on the new object'
class CoffeeOrder:
    def__init__(self,recipe,to_go=False):
        
SyntaxError: incomplete input
class CoffeeOrder:
    def__init__(self,recipe,to_go=False):
        
SyntaxError: incomplete input
class CoffeeOrder:
    def __init__(self,recipe,to_go=False):
        self.recipe = recipe
        self.to_go = to_go
    def brew(self):
        vessel = "in a cup" if self.to_go else "in a mug"
        print("Brewing" *self.recipe.parts,vessel)
class CoffeeRecipe:
    
SyntaxError: invalid syntax
class CoffeeOrder:
    def __init__(self,recipe,to_go=False):
        self.recipe = recipe
        self.to_go = to_go
    def brew(self):
        vessel = "in a cup" if self.to_go else "in a mug"
        print("Brewing" *self.recipe.parts,vessel)
class CoffeeRecipe:
    
SyntaxError: invalid syntax
class CoffeeOrder:
    def __init__(self,recipe,to_go=False):
        self.recipe = recipe
        self.to_go = to_go
    def brew(self):
        vessel = "in a cup" if self.to_go else "in a mug"
        print("Brewing" *self.recipe.parts,vessel)
class CoffeeRecipe:
    
SyntaxError: invalid syntax
class CoffeeOrder:
    def __init__(self,recipe,to_go=False):
        self.recipe = recipe
        self.to_go = to_go
    def brew(self):
        vessel = "in a cup" if self.to_go else "in a mug"
        print("Brewing" *self.recipe.parts,vessel)

        
class CoffeeRecipe:
    def __init__(self,parts):
        self.parts = parts

        
special = CoffeeRecipe(["double-shot","no-whip","latte","grande"])
order = CoffeeOrder(special,to_go=False)
another_order=CoffeeOrder(special,to_go=True)
another_order.brew()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    another_order.brew()
  File "<pyshell#31>", line 7, in brew
    print("Brewing" *self.recipe.parts,vessel)
TypeError: can't multiply sequence by non-int of type 'list'
class CoffeeRecipe:
    def __init__(self,parts):
        self.parts = partsclass CoffeeOrder:
            def __init__(self,recipe,to_go=False):
                self.recipe = recipe
                self.to_go = to_go
            def brew(self):
                vessel = "in a cup" if self.to_go else "in a mug"
                print("Brewing" *self.recipe.parts,vessel)
                
SyntaxError: invalid syntax
class CoffeeOrder:
    def __init__(self,recipe,to_go=False):
        self.recipe = recipe
        self.to_go = to_go
    def brew(self):
        vessel = "in a cup" if self.to_go else "in a mug"
        print("Brewing", *self.recipe.parts,vessel)

        
class CoffeeRecipe:
    def __init__(self,parts):
        self.parts = parts

        
special = CoffeeRecipe(["double-shot","no-whip","latte","grande"])
order = CoffeeOrder(special,to_go=False)
another_order=CoffeeOrder(special,to_go=True)
another_order.brew()
Brewing double-shot no-whip latte grande in a cup
order = CoffeeOrder(special,to_go=False)
order.brew()
Brewing double-shot no-whip latte grande in a mug
>>> import fumctools
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    import fumctools
ModuleNotFoundError: No module named 'fumctools'
>>> import functools
>>> def auto_order(to_go):
...     def decorator(cls):
...         @functools.wraps(cls)
...         def wrapper(*args,**kwargs):
...             recipe = cls(*args,**kwargs)
...             return(CoffeeOrder(recipe,to_go),recipe)
...         return wrapper
...     return decorator
... 
>>> @auto_order(to_go=True)
... class CoffeeShackRecipe(CoffeeRecipe):
...     pass
... order,recipe = CoffeeShackRecipe(["capucinno","mocha","latte"])
SyntaxError: invalid syntax
>>> @auto_order(to_go=True)
... class CoffeeShackRecipe(CoffeeRecipe):
...     pass
... 
>>> order,recipe = CoffeeShackRecipe(["capucinno","mocha","latte"])
>>> recipe.brew()
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    recipe.brew()
AttributeError: 'CoffeeShackRecipe' object has no attribute 'brew'
>>> recipe.parts()
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    recipe.parts()
TypeError: 'list' object is not callable
>>> recipe.parts
['capucinno', 'mocha', 'latte']
>>> order.brew()
Brewing capucinno mocha latte in a cup
