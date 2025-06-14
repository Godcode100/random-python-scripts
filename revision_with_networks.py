Python 3.11.4 (main, Jul  5 2023, 14:15:25) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
help(bytearray)

x = bytearray(b'Hello')
x[0]=72
print(x)
bytearray(b'Hello')
valid = False
while not valid:
    valid = input("Enter a number: ")
    if valid.isdigit():
        print(f"You entered {valid}")
    else:
        print(f"Entry ivalid try again")

        
Enter a number: abc
Entry ivalid try again
while not valid:
    valid = input("Enter a number: ")
    if valid.isdigit():
        print(f"You entered {valid}")
    else:
        print(f"Entry ivalid try again")

        

valid = False
while not valid:
    valid = input("Enter a number: ")
    if valid.isdigit():
        print(f"You entered {valid}")
    else:
        print(f"Entry ivalid try again")

        
Enter a number: 123
You entered 123
square = lambda z: z**2
result = square(6)
print(result)
36
students = [(mary,27),(John,23),(ric,12)]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    students = [(mary,27),(John,23),(ric,12)]
NameError: name 'mary' is not defined
students = [('mary',27),('John',23),('ric',12)]
students.sort(key=lambda c:c[1])
print(students)
[('ric', 12), ('John', 23), ('mary', 27)]

def factorial(n):
    if n ==0
    
SyntaxError: incomplete input
def factorial(n):
    if n ==0:
        return 1
    else:
        return n * factorial(n-1)

    
factorial(2)
2
factorial(3)
6
factorial (4)
24
factorial(0)
1
def num(w):
    return w * factorial(w-1)

num(3)
6
def num(w):
    return w * num(w-1)

num(3)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    num(3)
  File "<pyshell#42>", line 2, in num
    return w * num(w-1)
  File "<pyshell#42>", line 2, in num
    return w * num(w-1)
  File "<pyshell#42>", line 2, in num
    return w * num(w-1)
  [Previous line repeated 1023 more times]
RecursionError: maximum recursion depth exceeded
def factorial(n):
    if n ==-2:
        return 1
    else:
        return n * factorial(n-1)

    
factorial(-1)
-1
factorial(5)
0
def factorial(n):
    if n ==-10:
        return 1
    else:
        return n * factorial(n-1)

    
factorial(-7)
-504
factorial(7)
0
def square(x):
    x = x**2
    return x
square(5)
SyntaxError: invalid syntax
def square(x):
    x = x**2
    return x
square(5)
SyntaxError: invalid syntax
def square(x):
    x = x**2
    return x

square(5)
25
number = 5
square(number)
25
print(number)
5
def outer():
    def inner():
        print('This is inside')
    return inner
function = outer()
SyntaxError: invalid syntax
def outer():
    def inner():
        print('This is inside')
    return inner

function = outer()
print(function)
<function outer.<locals>.inner at 0x7f415405d4e0>
function()
This is inside
outside = outer()
outside()
This is inside
>>> file = open('ex13.py','r')
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    file = open('ex13.py','r')
FileNotFoundError: [Errno 2] No such file or directory: 'ex13.py'
>>> file = open('log.txt','r')
>>> contents = file.read()
>>> print(contents)

>>> file.close()
>>> file = open('landmarks.py','r')
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    file = open('landmarks.py','r')
FileNotFoundError: [Errno 2] No such file or directory: 'landmarks.py'
>>> file = open('log2.txt','r')
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    file = open('log2.txt','r')
FileNotFoundError: [Errno 2] No such file or directory: 'log2.txt'
>>> with open("Desktop/landmarks.py",'r') as file:
...     contents = file.read()
...     print(contents)
... 
...     
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    with open("Desktop/landmarks.py",'r') as file:
FileNotFoundError: [Errno 2] No such file or directory: 'Desktop/landmarks.py'
>>> with open("landmarks.py",'r') as file:
...     contents = file.read()
...     print(contents)
... 
...     
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    with open("landmarks.py",'r') as file:
FileNotFoundError: [Errno 2] No such file or directory: 'landmarks.py'
