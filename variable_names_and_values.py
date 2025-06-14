Python 3.11.4 (main, Jul  5 2023, 14:15:25) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
The is operator compares identity the specific location in memory that a name is bound to.
SyntaxError: invalid syntax
#The is operator compares identity the specific location in memory that a name is bound to.
#This means is doesnt check whethera name points to equivalent values but rather whether it points to the same value in memory
spam = 12345
maps = spam
eggs = 12345
print(spam == maps)
True
print(spam == eggs)
True
answer = 42
insight = 42
print(spam is maps)
True
print(spam is eggs)
False
print(answer == insight)
True
#Checking the sneakiness of is opeartor
print(answer is insight)
True
#Only use the is opeartor to check if something is None
#As a matter of fact python has the id() builtin function that returns an integer of whatever is passed to it
#These values are what is operator compares
id(answer)
8886312
id(me)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    id(me)
NameError: name 'me' is not defined
id(insight)
8886312
id(spam)
140443946596432
id(maps)
140443946596432
id(eggs)
140443935412208
#if you ever need to know the data type of a name
#use type(), remember everything is an object in python so this returns what class the name is an instance of
type(answer)
<class 'int'>
#On rare occasions you may want to check datatype before you do something
#for that you can use the is operator
if type(answer) is int:
    print('answer is of type integer class')

    
answer is of type integer class
#However it maybe necessary to use isinstance() instead of type() as it accounts for subclasses and inheritance
#The isinstance () returns True or False so can be used as a condition in if statement
if isinstance(answer,int):
    print("answer is an integer")

    
answer is an integer

def spam():
    message = "Spam"
    word = "spam"
    for _ in range(100):
        seperator = ","
        message+=seperator+word
    message +=seperator
    message+="spam!"
    return message
spam()
SyntaxError: invalid syntax
spam=spam()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    spam=spam()
TypeError: 'int' object is not callable
qw=spam()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    qw=spam()
TypeError: 'int' object is not callable
spam()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    spam()
TypeError: 'int' object is not callable
def spam():
    message = "Spam"
    word = "spam"
    for _ in range(100):
        seperator = ","
        message+=seperator+word
    message +=seperator
    message+="spam!"
return message
SyntaxError: invalid syntax
def spam():
    message = "Spam"
    word = "spam"
    for _ in range(100):
        seperator = ","
        message+=seperator+word
    message +=seperator
    message+="spam!"
    return message
spam()
SyntaxError: invalid syntax
def spam():
    message = "Spam"
    word = "spam"
    for _ in range(100):
        seperator = ","
        message+=seperator+word
    message +=seperator
    message+="spam!"
return message
SyntaxError: invalid syntax
def spam():
    message = "Spam"
    word = "spam"
    for _ in range(100):
        seperator = ","
        message+=seperator+word
    message +=seperator
    message+="spam!"
    print(message)
spam()
SyntaxError: invalid syntax
def spam():
    message = "Spam"
    word = "spam"
    for _ in range(100):
        seperator = ","
        message+=seperator+word
    message +=seperator
    message+="spam!"
    return message
out=spam()
SyntaxError: invalid syntax
print(out)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    print(out)
NameError: name 'out' is not defined. Did you mean: 'oct'?
def spam():
def spam():
    message = "Spam"
    word = "spam"
    for _ in range(100):
        seperator = ","
        message+=seperator+word
        message +=seperator
    message+="spam!"
    return message
SyntaxError: expected an indented block after function definition on line 1
def spam():
    message = "Spam"
    word = "spam"
    for _ in range(100):
        seperator = ","
        message+=seperator+word
    message +=seperator
    message+="spam!"
    return message

out=spam()
print(out)
Spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam,spam!
help(atexit)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    help(atexit)
NameError: name 'atexit' is not defined. Did you mean: 'anext'?
help(atexit())
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    help(atexit())
NameError: name 'atexit' is not defined. Did you mean: 'anext'?
help(anext)
Help on built-in function anext in module builtins:

anext(...)
    async anext(aiterator[, default])
    
    Return the next item from the async iterator.  If default is given and the async
    iterator is exhausted, it is returned instead of raising StopAsyncIteration.

atexit()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    atexit()
NameError: name 'atexit' is not defined. Did you mean: 'anext'?
atexit.register()
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    atexit.register()
NameError: name 'atexit' is not defined. Did you mean: 'anext'?
#global and local scope
high score = 456
SyntaxError: invalid syntax
high_score=456
def score():
    new_score=300
    if new_score > high_score:
        print("New High")
    else:
        print("Work harder")

        
score()
Work harder
def score():
    new_score=3000
    if new_score > high_score:
        print("New High")
    else:
        print("Work harder")

        
score()
New High
def score():
    new_score=3000
    if new_score > high_score:
        print("New High")
        high_score = new_score
    else:
        print("Work harder")

    
score()
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    score()
  File "<pyshell#86>", line 3, in score
    if new_score > high_score:
UnboundLocalError: cannot access local variable 'high_score' where it is not associated with a value

high_score=456
def score():
    new_score=300
    if new_score > high_score:
        print("New High")
    else:
        print("Work harder")

SyntaxError: multiple statements found while compiling a single statement


def score():
    new_score=300
    if new_score > high_score:
        print("New High")
    else:
        print("Work harder")

        
score*()
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    score*()
TypeError: can't multiply sequence by non-int of type 'function'
score()
Work harder
def score():
    new_score=300
    if new_score > high_score:
        print("New High")
        high_score = new_score
    else:
        print("Work harder")

        
score()
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    score()
  File "<pyshell#97>", line 3, in score
    if new_score > high_score:
UnboundLocalError: cannot access local variable 'high_score' where it is not associated with a value
def score():
    new_score=300
    if new_score > high_score:
        print("New High")
        print(high_score)
    else:
        print("Work harder")

        
score()
Work harder
def score():
    new_score=3000
    if new_score > high_score:
        print("New High")
        print(high_score)
    else:
        print("Work harder")

score()
New High
456

def score():
    new_score=3000
    if new_score > high_score:
        print("New High")
        high_sco = new_score
    else:
        print("Work harder")

        
score()
New High
print(high_sco)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    print(high_sco)
NameError: name 'high_sco' is not defined. Did you mean: 'high_score'?
def score():
    new_score=3000
    if new_score > high_score:
        print("New High")
        high_sco = new_score
        print(high_sco)
    else:
        print("Work harder")

        
score()
New High
3000
#Every time you wish to rebind a global name from within a local scope,
#you must use the global keyword first.
def score():
    global high_score
    new_score=3000
    if new_score > high_score:
        print("New High")
        high_score = new_score
        print(high_score)
    else:
        print("Work harder")

        
score()
New High
3000
#The nonlocal Keyword
#Python allows you to write functions within functions.
spam = True
def order():
    eggs = 12
    def cook():
        nonlocal eggs
        if spam:
            print("Spam ...!")
        eggs-=1
    cook()

    
order()
Spam ...!

def order():
    eggs = 12
    print(eggs)
    def cook():
        nonlocal eggs
        if spam:
            print("Spam ...!")
        eggs-=1
    cook()

   
order()
SyntaxError: invalid syntax
spam = True
def order():
    eggs = 12
    print(eggs)
    def cook():
        nonlocal eggs
        if spam:
            print("Spam ...!")
        eggs-=1
    cook()
    
SyntaxError: multiple statements found while compiling a single statement

def order():
    eggs = 12
    def cook():
        nonlocal eggs
        if spam:
            print("Spam ...!")
        eggs-=1
    cook()

    
order()
Spam ...!
def order():
    eggs = 12
    prnt(eggs)
    def cook():
        nonlocal eggs
        if spam:
            print("Spam ...!")
        eggs-=1
    cook()

    
order()
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    order()
  File "<pyshell#134>", line 3, in order
    prnt(eggs)
NameError: name 'prnt' is not defined. Did you mean: 'print'?
def order():
    eggs = 12
    print(eggs)
    def cook():
        nonlocal eggs
        if spam:
            print("Spam ...!")
        eggs-=1
    cook()

    
order()
12
Spam ...!
def order():
    eggs = 12
    print(eggs)
    def cook():
        nonlocal eggs
        if spam:
            print("Spam ...!")
        eggs-=1
    cook()
    print(eggs)

    
order()
12
Spam ...!
11
#The function order() contains another function: cook(). Each function
#has its own scope.
#Remember, as long as a function only accesses a global name like spam,
#you don’t need to do anything special. However, trying to assign to a global
#name will actually define a new local name that shadows the global one.
#The same behavior is true of the inner function using names defined in the
#outer function, which is known as the nested scope or enclosing scope. To
#get around this, I specify that eggs is nonlocal, meaning it can be found in
#the enclosing scope, rather than in the local scope ❶. The inner function
#cook() has no trouble accessing the global name spam.

"""THE CURIOUS CASE OF CLASSES"""
'THE CURIOUS CASE OF CLASSES'
#Classes have their own way of dealing with scope. Technically speaking,
#classes don’t directly factor into the scope resolution order.
#Every name declared directly in a class is known as an attribute
class Nutrimatic:
    output ="Something almost but not quite, unlike tea"

    
class Nutrimatic:
    output = "Something almost but not quite unlike tea"
    def mixed(self,beverage):
        self.output

        
machine = Nutrimatic()
mug = machine.mixed(Tea)
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    mug = machine.mixed(Tea)
NameError: name 'Tea' is not defined
mug =machine.mixed(beverage)
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    mug =machine.mixed(beverage)
NameError: name 'beverage' is not defined
mug = machine.mixed("Tea")
print(mug)
None
class Nutrimatic:
    output = "Something almost but not quite unlike Tea"
    def mixed(self,beverage):
        return self.output

    
machine = Nutrimatic()
mug = machine.mixed("Tea")
print(mug)
Something almost but not quite unlike Tea
print(output)
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    print(output)
NameError: name 'output' is not defined
print(Nutrimatic.output)
Something almost but not quite unlike Tea
print(machine)
<__main__.Nutrimatic object at 0x7fbba81d0d10>
print(machine.output)
Something almost but not quite unlike Tea
#self refers to the class instance,the function(instance method),request is being called on.
"""THE IMMUTABLE TRUTH"""
'THE IMMUTABLE TRUTH'
Values in pyhton are either mutable or immutable
SyntaxError: invalid syntax
#Values in python are either mutable or immutable
#Immutable values cannot be changed in place and include: integers,strings,floatin-point numbers and tuples
eggs =12
carton = eggs
print(carton is eggs)
True
print(carton,eggs)
12 12
eggs+=1
print(carton is eggs)
False
print(eggs,carton)
13 12

#Mutable values on the other hand can be changed in place
#an example are lists
temps=[72,91,22}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
temps=[72,92,22]
highs = temps
print(highs is temps)
True
print(highs,temps)
[72, 92, 22] [72, 92, 22]
temps=+[88]
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    temps=+[88]
TypeError: bad operand type for unary +: 'list'
>>> temps+=[88]
>>> print(highs is temps)
True
>>> print(highs,temps)
[72, 92, 22, 88] [72, 92, 22, 88]
>>> 
>>> 
>>> """PASSING BY ASSIGNMENT"""
'PASSING BY ASSIGNMENT'
>>> #Does pass python pass by value or by reference ?the answer is neither
>>> #Python passes by assignment
>>> #consider the function below:
>>> def greeta(person):
...     print(f"Hello {person}")
... 
>>> my_name ="Jason"
>>> greeta(my_name)
Hello Jason
>>> there is one copy of the string value"Jason" and it is bound to the name my_name
SyntaxError: invalid syntax
>>> #there is one copy of the string value"Jason" and it is bound to the name my_name
>>> #if i pass my_name to function greeta specifically the parameter person it is as if am saying person=my_name
>>> #assignment never makes a copy of a value but rather person is now bound to the value "Jason"
>>> 
>>> 
>>> """functions should not have side effects,"""
'functions should not have side effects,'
>>> #here we have a function that sorts a list an prints the lowest number
>>> print(temps)
[72, 92, 22, 88]
>>> def find_lowest(temperatures)
SyntaxError: incomplete input
>>> def find_lowest(temperatures):
...     temperatures.sort()
...     print(temperatures)
... 
...     
>>> find_lowest(temps)
[22, 72, 88, 92]
>>> #this is a clear example of list having side effects
>>> #bse temp is no longer the same
>>> print(temps)
[22, 72, 88, 92]
>>> #To avoid this we have to use sorted that creates a new list
>>> def find_lowest(temperatures):
...     sorted_temps = sorted(temperatures)
...     print(sorted_temps)
... 
...     
>>> print(highs)
[22, 72, 88, 92]
>>> board =[["-"]*3]
>>> print(board)
[['-', '-', '-']]
>>> boards = [["-"]*3]*3
>>> print(boards)
[['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
