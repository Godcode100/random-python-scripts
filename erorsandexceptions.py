Python 3.11.4 (main, Jul  5 2023, 14:15:25) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
"""In many languagues exceptions are regarded as the archnemeses of programmers and the hallmarks of some degree of failure. Something somewhere was used improperly.Python developers on the otherhand recognise exceptions as friends that help write better code."""
'In many languagues exceptions are regarded as the archnemeses of programmers and the hallmarks of some degree of failure. Something somewhere was used improperly.Python developers on the otherhand recognise exceptions as friends that help write better code.'

"""Lets demonstrate what exceptions look like in python and how to read their accompanying messages. We cover catching exceptions,handling them and raising them"""
'Lets demonstrate what exceptions look like in python and how to read their accompanying messages. We cover catching exceptions,handling them and raising them'


"""An exception is an interuption in normal processing typically caused by an error condition, that can be handled by another part of the program."""
'An exception is an interuption in normal processing typically caused by an error condition, that can be handled by another part of the program.'


import random
def generate_puzzle(low=1,high=100):
    pass
def make_guess(target):
    
SyntaxError: invalid syntax
def generate_puzzle(low=1,high=100):
    pass

def make_guess(target):
    guess = int(input("Guess "))
    if guess == target:
        return True
    if guess > target:
        print(f"{guess} is too high")
    if guess < target:
        print(f"{guess} is too low")

        
def play(tries=8):
    target = generate_puzzle()
    while tries > 0:
        if make_guess(target):
            print("You win")
            return
        tries -= 1
        print(f"{tries} tries left")
    print(f"Gameover!. The answer was {target}")

    
def generate_puzzle(low=1,high=100):
    print(f"I am thinking of a number between {low} and {high}")
    return random.randint(low,high)
def play(tries=8):
    target = generate_puzzle()
    while tries > 0:
        if make_guess(target):
            print("You win")
            return
        tries -= 1
        print(f"{tries} tries left")
    print(f"Gameover!. The answer was {target}")
    
SyntaxError: invalid syntax
def generate_puzzle(low=1,high=100):
    print(f"I am thinking of a number between {low} and {high}")
    return random.randint(low,high)
def play(tries=8):
    target = generate_puzzle()
    while tries > 0:
        if make_guess(target):
            print("You win")
            return
        tries -= 1
        print(f"{tries} tries left")
    print(f"Gameover!. The answer was {target}")
    
SyntaxError: invalid syntax
def generate_puzzle(low=1,high=100):
    print(f"I am thinking of a number between {low} and {high}")
    return random.randint(low,high)


def play(tries=8):
    target = generate_puzzle()
    while tries > 0:
        if make_guess(target):
            print("You win")
            return
        tries -= 1
        print(f"{tries} tries left")
    print(f"Gameover!. The answer was {target}")

    
play()
I am thinking of a number between 1 and 100
Guess 7
7 is too low
7 tries left
Guess 60
60 is too low
6 tries left
Guess 90
90 is too high
5 tries left
Guess 84
84 is too high
4 tries left
Guess 78
78 is too high
3 tries left
Guess 68
68 is too high
2 tries left
Guess 63
63 is too high
1 tries left
Guess 61
61 is too low
0 tries left
Gameover!. The answer was 62
play()
I am thinking of a number between 1 and 100
Guess 50
50 is too high
7 tries left
Guess 35
35 is too low
6 tries left
Guess 25
25 is too low
5 tries left
Guess 30
30 is too low
4 tries left
Guess 33
33 is too low
3 tries left
Guess 34
34 is too low
2 tries left
Guess 45
45 is too high
1 tries left
Guess 43
43 is too low
0 tries left
Gameover!. The answer was 44
play()
I am thinking of a number between 1 and 100
Guess 50
50 is too low
7 tries left
Guess 70
70 is too high
6 tries left
Guess 65
65 is too low
5 tries left
Guess 67
67 is too low
4 tries left
Guess 69
You win
play()
I am thinking of a number between 1 and 100
Guess -1
-1 is too low
7 tries left
Guess one
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    play()
  File "<pyshell#39>", line 4, in play
    if make_guess(target):
  File "<pyshell#21>", line 2, in make_guess
    guess = int(input("Guess "))
ValueError: invalid literal for int() with base 10: 'one'

"""The block of code we receive when an error occurs is called a Traceback."""
'The block of code we receive when an error occurs is called a Traceback.'
play()
I am thinking of a number between 1 and 100
Guess 
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    play()
  File "<pyshell#39>", line 4, in play
    if make_guess(target):
  File "<pyshell#21>", line 2, in make_guess
    guess = int(input("Guess "))
ValueError: invalid literal for int() with base 10: ''

"""In python we dont prevent errors we embrace them using try statements to handle exceptional situations."""
'In python we dont prevent errors we embrace them using try statements to handle exceptional situations.'
def make_guess(target):
    guess = None
    while guess is None:
        try:
            guess = int(input("Guess:"))
        except ValueError:
            print("Enter an integer")
    if guess == target:
        return True
    if guess > target:
        print(f"{guess} is too high")
    if guess < target:
        print(f"{guess} is too low")

        
def play(tries=8):
    target = generate_puzzle()
    while tries > 0:
        if make_guess(target):
            print("You win")
            return
        tries -= 1
        print(f"{tries} tries left")
    print(f"Gameover!. The answer was {target}")

    
play()
I am thinking of a number between 1 and 100
Guess:
Enter an integer
Guess:Fifty
Enter an integer
Guess:
Enter an integer
Guess:80
80 is too high
7 tries left
Guess:00
0 is too low
6 tries left
Guess:00
0 is too low
5 tries left
Guess:00
0 is too low
4 tries left
Guess:-9
-9 is too low
3 tries left
Guess:0
0 is too low
2 tries left
Guess:0
0 is too low
1 tries left
Guess:0
0 is too low
0 tries left
Gameover!. The answer was 54
>>> help(.isdigit)
SyntaxError: invalid syntax
>>> help(isdigit)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    help(isdigit)
NameError: name 'isdigit' is not defined
>>> guess.isdigit()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    guess.isdigit()
NameError: name 'guess' is not defined
>>> 
>>> """mULTIPLE EXCEPTIONS"""
'mULTIPLE EXCEPTIONS'
>>> 
>>> class AverageCalculator:
...     def __init__(self):
...         self.total = 0
...         self.count = 0
...     def __call__(self,*values):
...         if values:
...             for value in values:
...                 self.total += float(value)
...                 self.count += 1
...             return self.total / self.count
... 
...         
>>> 
>>> average =AverageCalculator()
>>> values = input("Enter scores seperated by space:\n ").split()
Enter scores seperated by space:
 60 70 90 89 45
>>> try:
...     print(f"Average is {average(*values)}")
... except ZeroDivisionError:
...     print("No values provided")
... except (ValueError,UnicodeError):
