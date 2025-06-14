Python 3.11.4 (main, Jul  5 2023, 14:15:25) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
#!/usr/bin/env python3
def open():
    print("Ahhhhhhhhh!")

    
def close():
    print("Thank you for making a simple door happy")

    
import os
help(os)

import math
help(math)

x=math.pow(6,3)
print(x)
216.0
x=math.prod([3,4])
print(x)
12
import *
SyntaxError: incomplete input
import print
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    import print
ModuleNotFoundError: No module named 'print'
help(print)
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.
    
    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.

from math import *
import sys
print(sys.path)
['', '/home/joelouma/sessions', '/home/joelouma/anaconda3/bin', '/home/joelouma/anaconda3/lib/python311.zip', '/home/joelouma/anaconda3/lib/python3.11', '/home/joelouma/anaconda3/lib/python3.11/lib-dynload', '/home/joelouma/anaconda3/lib/python3.11/site-packages']
>>> help(import)
SyntaxError: invalid syntax
>>> help(__import__())
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    help(__import__())
TypeError: __import__() missing required argument 'name' (pos 1)
>>> help(__import__(math))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    help(__import__(math))
TypeError: module name must be a string
>>> help(__import__('math'))

>>> help(__import__)
Help on built-in function __import__ in module builtins:

__import__(name, globals=None, locals=None, fromlist=(), level=0)
    Import a module.
    
    Because this function is meant for use by the Python
    interpreter and not for general use, it is better to use
    importlib.import_module() to programmatically import a module.
    
    The globals argument is only used to determine the context;
    they are not modified.  The locals argument is unused.  The fromlist
    should be a list of names to emulate ``from name import ...``, or an
    empty list to emulate ``import name``.
    When importing a module from a package, note that __import__('A.B', ...)
    returns package A when fromlist is empty, but its submodule B when
    fromlist is not empty.  The level argument is used to determine whether to
    perform absolute or relative imports: 0 is absolute, while a positive number
    is the number of parent directories to search relative to the current module.

>>> importlib
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    importlib
NameError: name 'importlib' is not defined
>>> importlib.import_module(pow)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    importlib.import_module(pow)
NameError: name 'importlib' is not defined
>>> importlib.import_module(pow,math)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    importlib.import_module(pow,math)
NameError: name 'importlib' is not defined
>>> print(sys.meta_path)
[<_distutils_hack.DistutilsMetaFinder object at 0x7f189801a790>, <class '_frozen_importlib.BuiltinImporter'>, <class '_frozen_importlib.FrozenImporter'>, <class '_frozen_importlib_external.PathFinder'>]
>>> print(sys.modules)

