Python 3.11.4 (main, Jul  5 2023, 14:15:25) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
name = "Jason"
if name != "";
SyntaxError: incomplete input
if name != '':
    message = "Hello " + name + "!"
    print (message)

    
Hello Jason!
raining = True
hailing = False
if raining:
    if hailing:
        print("NOPE")
    else:
        print("Umnbrell time")

        
Umnbrell time
DOING NOTHING
SyntaxError: incomplete input
if raining:
    pass
raining = True
SyntaxError: invalid syntax
raining = True
if raining:
    pass

print("#Uganda")
#Uganda
def make_tea():
    """Will produce a tea like concotion
    that is sweet"""
    pass
print(make_tea.__doc__)
SyntaxError: invalid syntax
make_tea
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    make_tea
NameError: name 'make_tea' is not defined
make_tea()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    make_tea()
NameError: name 'make_tea' is not defined
def make_coffee():
    """Uganda cash crop"""
    print("coffee")

    
make_coffee()
coffee
print(make_coffee.__doc__)
Uganda cash crop

====================================================================================== RESTART: Shell =====================================================================================
help(make_coffee)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    help(make_coffee)
NameError: name 'make_coffee' is not defined
def make_coffee():
    """Cashcrop in Uuganda"""
    print("Coffee Uganda")

    
make_coffee()
Coffee Uganda
help(make_coffee)
Help on function make_coffee in module __main__:

make_coffee()
    Cashcrop in Uuganda

print(make_coffee.__doc__)
Cashcrop in Uuganda
position = 200
print(type(position))
<class 'int'>
position = 3000000000000
print(type(position))
<class 'int'>
position = "Jesus"
print(type(position))
<class 'str'>
position = float("nan")
position
nan
float("nan")
nan
float("inf")
inf
from decimal import Decimal
from fraction import Fraction
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    from fraction import Fraction
ModuleNotFoundError: No module named 'fraction'
from decimal import Decimal
from fractions import Fraction
third_fraction = Fraction(1,5)
print(third_fraction)
1/5
third_third = Fraction(2,0)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    third_third = Fraction(2,0)
  File "/home/joelouma/anaconda3/lib/python3.11/fractions.py", line 157, in __new__
    raise ZeroDivisionError('Fraction(%s, 0)' % numerator)
ZeroDivisionError: Fraction(2, 0)
third_fraction = Fraction(2,7)
print(third_fraction)
2/7
third_fraction = Fraction(7,2)
print(third_fraction)
7/2
third_fraction=Fraction(7,2,_normalize=False)
print(third_fraction)
7/2
third_fraction=Fraction(2,1,3)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    third_fraction=Fraction(2,1,3)
TypeError: Fraction.__new__() takes from 1 to 3 positional arguments but 4 were given
third_fraction=Fraction(numerator=1,denominator=3,4)
SyntaxError: positional argument follows keyword argument
third_fraction=Fraction(numerator=1,denominator=3)
print(third_fraction)
1/3
third_decimal=Decimal("0.333")
print(third_decimal)
0.333
third_float=1/3
print(third_float)
0.3333333333333333
num=36j
print(num)
36j
print(type(num))
<class 'complex'>
print(1234 / 149)
8.281879194630873
print(1234 % 149)
42
print(--42)
42
print(1234 // 149)
8
print(144/12)
12.0
print(144%12)
0
print(144/15)
9.6
print(15*9)
135
print(144-135)
9
print(9/15)
0.6
print(144%15)
9
print(5/2)
2.5
print(5//2)
2
print(5%2)
1
c=divmod(5,2)
print(c)
(2, 1)
infinity = float("inf")
print(infinity)
inf
import math
print(math.pi)
3.141592653589793
print(math.tau)
6.283185307179586
print(math.e)
2.718281828459045
print(math.inf)
inf
print(math.nan)
nan
KeyboardInterrupt
print(math.pi)
3.141592653589793
#calculating something using distance to it and angle from vantage point to top of object
distance_ft = 65
angle_deg = 74
#convert deg to radians
angle_rad = math.radians(angle_deg)
#height
height_ft = distance_ft * math.tan(angle_rad)
height_ft = round(height_ft,1)#round to one decimal place
print(height_ft)
226.7
command = "greet"
if command == "greet":
    print("Hello")
elif command =="exit":
    print("Goodbye")
else:
    print("I dont Understand")

Hello
score=98
high_score = 100
print(score == high_score)
False
print(score != high_score)
True
print(score > high_score)
False
print(score < high_score)
True
print(score <> high_score)
SyntaxError: invalid syntax
print(score <= high_score)
True
print(score >= high_score)
False
#Python 3.8 introduced assignment expressions, which allow you to assign a
#value to a variable and use that variable in another expression at the same
#time. This is possible with the so-called walrus operator (:=)

if (eggs:=7+5)==12:
    print(eggs)

12
print(eggs)
12
if (eggs:=7+5)==12:
    print("we have a dozen eggs")

we have a dozen eggs
import textwrap
parrot = """
This parrot is no more!
He has ceased to be!
He's expired
and gone to meet his maker!
He's a stiff!
Bereft of life,
he rests in peace!"""
print(parrot)

This parrot is no more!
He has ceased to be!
He's expired
and gone to meet his maker!
He's a stiff!
Bereft of life,
he rests in peace!
me=parrot.textwrap.TextWrapper(10))
SyntaxError: unmatched ')'
me=parrot.textwrap.TextWrapper(10)
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    me=parrot.textwrap.TextWrapper(10)
AttributeError: 'str' object has no attribute 'textwrap'
me=textwrap.TextWrapper(10))
SyntaxError: unmatched ')'
me=textwrap.TextWrapper(10)
print(parrot.me())
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    print(parrot.me())
AttributeError: 'str' object has no attribute 'me'
print(parrot(me))
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    print(parrot(me))
TypeError: 'str' object is not callable
print(me.parrot)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    print(me.parrot)
AttributeError: 'TextWrapper' object has no attribute 'parrot'
print(me)
<textwrap.TextWrapper object at 0x7f4dc40b39d0>
help(textwrap)
Help on module textwrap:

NAME
    textwrap - Text wrapping and filling.

MODULE REFERENCE
    https://docs.python.org/3.11/library/textwrap.html
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

CLASSES
    builtins.object
        TextWrapper
    
    class TextWrapper(builtins.object)
     |  TextWrapper(width=70, initial_indent='', subsequent_indent='', expand_tabs=True, replace_whitespace=True, fix_sentence_endings=False, break_long_words=True, drop_whitespace=True, break_on_hyphens=True, tabsize=8, *, max_lines=None, placeholder=' [...]')
     |  
     |  Object for wrapping/filling text.  The public interface consists of
     |  the wrap() and fill() methods; the other methods are just there for
     |  subclasses to override in order to tweak the default behaviour.
     |  If you want to completely replace the main wrapping algorithm,
     |  you'll probably have to override _wrap_chunks().
     |  
     |  Several instance attributes control various aspects of wrapping:
     |    width (default: 70)
     |      the maximum width of wrapped lines (unless break_long_words
     |      is false)
     |    initial_indent (default: "")
     |      string that will be prepended to the first line of wrapped
     |      output.  Counts towards the line's width.
     |    subsequent_indent (default: "")
     |      string that will be prepended to all lines save the first
     |      of wrapped output; also counts towards each line's width.
     |    expand_tabs (default: true)
     |      Expand tabs in input text to spaces before further processing.
     |      Each tab will become 0 .. 'tabsize' spaces, depending on its position
     |      in its line.  If false, each tab is treated as a single character.
     |    tabsize (default: 8)
     |      Expand tabs in input text to 0 .. 'tabsize' spaces, unless
     |      'expand_tabs' is false.
     |    replace_whitespace (default: true)
     |      Replace all whitespace characters in the input text by spaces
     |      after tab expansion.  Note that if expand_tabs is false and
     |      replace_whitespace is true, every tab will be converted to a
     |      single space!
     |    fix_sentence_endings (default: false)
     |      Ensure that sentence-ending punctuation is always followed
     |      by two spaces.  Off by default because the algorithm is
     |      (unavoidably) imperfect.
     |    break_long_words (default: true)
     |      Break words longer than 'width'.  If false, those words will not
     |      be broken, and some lines might be longer than 'width'.
     |    break_on_hyphens (default: true)
     |      Allow breaking hyphenated words. If true, wrapping will occur
     |      preferably on whitespaces and right after hyphens part of
     |      compound words.
     |    drop_whitespace (default: true)
     |      Drop leading and trailing whitespace from lines.
     |    max_lines (default: None)
     |      Truncate wrapped lines.
     |    placeholder (default: ' [...]')
     |      Append to the last line of truncated text.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, width=70, initial_indent='', subsequent_indent='', expand_tabs=True, replace_whitespace=True, fix_sentence_endings=False, break_long_words=True, drop_whitespace=True, break_on_hyphens=True, tabsize=8, *, max_lines=None, placeholder=' [...]')
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  fill(self, text)
     |      fill(text : string) -> string
     |      
     |      Reformat the single paragraph in 'text' to fit in lines of no
     |      more than 'self.width' columns, and return a new string
     |      containing the entire wrapped paragraph.
     |  
     |  wrap(self, text)
     |      wrap(text : string) -> [string]
     |      
     |      Reformat the single paragraph in 'text' so it fits in lines of
     |      no more than 'self.width' columns, and return a list of wrapped
     |      lines.  Tabs in 'text' are expanded with string.expandtabs(),
     |      and all other whitespace characters (including newline) are
     |      converted to space.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  sentence_end_re = re.compile('[a-z][\\.\\!\\?][\\"\\\']?\\Z')
     |  
     |  unicode_whitespace_trans = {9: 32, 10: 32, 11: 32, 12: 32, 13: 32, 32:...
     |  
     |  wordsep_re = re.compile('\n        ( # any whitespace\n      ...# word...
     |  
     |  wordsep_simple_re = re.compile('([\\\t\\\n\\\x0b\\\x0c\\\r\\ ]+)')

FUNCTIONS
    dedent(text)
        Remove any common leading whitespace from every line in `text`.
        
        This can be used to make triple-quoted strings line up with the left
        edge of the display, while still presenting them in the source code
        in indented form.
        
        Note that tabs and spaces are both treated as whitespace, but they
        are not equal: the lines "  hello" and "\thello" are
        considered to have no common leading whitespace.
        
        Entirely blank lines are normalized to a newline character.
    
    fill(text, width=70, **kwargs)
        Fill a single paragraph of text, returning a new string.
        
        Reformat the single paragraph in 'text' to fit in lines of no more
        than 'width' columns, and return a new string containing the entire
        wrapped paragraph.  As with wrap(), tabs are expanded and other
        whitespace characters converted to space.  See TextWrapper class for
        available keyword args to customize wrapping behaviour.
    
    indent(text, prefix, predicate=None)
        Adds 'prefix' to the beginning of selected lines in 'text'.
        
        If 'predicate' is provided, 'prefix' will only be added to the lines
        where 'predicate(line)' is True. If 'predicate' is not provided,
        it will default to adding 'prefix' to all non-empty lines that do not
        consist solely of whitespace characters.
    
    shorten(text, width, **kwargs)
        Collapse and truncate the given text to fit in the given width.
        
        The text first has its whitespace collapsed.  If it then fits in
        the *width*, it is returned as is.  Otherwise, as many words
        as possible are joined and then the placeholder is appended::
        
            >>> textwrap.shorten("Hello  world!", width=12)
            'Hello world!'
            >>> textwrap.shorten("Hello  world!", width=11)
            'Hello [...]'
    
    wrap(text, width=70, **kwargs)
        Wrap a single paragraph of text, returning a list of wrapped lines.
        
        Reformat the single paragraph in 'text' so it fits in lines of no
        more than 'width' columns, and return a list of wrapped lines.  By
        default, tabs in 'text' are expanded with string.expandtabs(), and
        all other whitespace characters (including newline) are converted to
        space.  See TextWrapper class for available keyword args to customize
        wrapping behaviour.

DATA
    __all__ = ['TextWrapper', 'wrap', 'fill', 'dedent', 'indent', 'shorten...

FILE
    /home/joelouma/anaconda3/lib/python3.11/textwrap.py


me=textwrap.TextWrapper(parrot,10))
                                
SyntaxError: unmatched ')'
me=textwrap.TextWrapper(parrot,10)
                                
print(me)
                                
<textwrap.TextWrapper object at 0x7f4dc52993d0>
me=textwrap.dedent(parrot)
                                
print(me)
                                

This parrot is no more!
He has ceased to be!
He's expired
and gone to meet his maker!
He's a stiff!
Bereft of life,
he rests in peace!
me=textwrap.TextWrapper(parrot)
                                
print(me)
                                
<textwrap.TextWrapper object at 0x7f4dc40ae0d0>
me=textwrap.wrap(parrot,10)
                                
print(me)
                                
[' This', 'parrot is', 'no more!', 'He has', 'ceased to', "be! He's", 'expired', 'and gone', 'to meet', 'his maker!', "He's a", 'stiff!', 'Bereft of', 'life, he', 'rests in', 'peace!']
me=textwrap.wrap(parrot,15)
                                
print(me)
                                
[' This parrot is', 'no more! He has', 'ceased to be!', "He's expired", 'and gone to', 'meet his maker!', "He's a stiff!", 'Bereft of life,', 'he rests in', 'peace!']
me=textwrap.shorten(parrot,15)
                                
print(me)
                                
This [...]
me=textwrap.fill(parrot,10)
                                
print(me)
                                
 This
parrot is
no more!
He has
ceased to
be! He's
expired
and gone
to meet
his maker!
He's a
stiff!
Bereft of
life, he
rests in
peace!
my name = "God" "Code" "100"
                                
SyntaxError: invalid syntax
name = "God" "Code" "100"
                                
print(name)
                                
GodCode100
name = ("God" "Code" "100")
                                
print(name)
                                
GodCode100
name = {"God" "Code" "100"}
                                
print(name)
                                
{'GodCode100'}
name = {"God" "Code" "100"}
                                
name = "God" "Code" "100")
                                    
SyntaxError: unmatched ')'
name = ("God" "Code" "100")
                                    
name= ("God"
       "name"
       "100")
                                    
print(name)
                                    
Godname100
print(f"{5+5=}")
                                    
5+5=10
print(f"5+5=")
                                    
5+5=
print(f'{6^2}')
                                    
4
6**2
                                    
36
2^2
                                    
0
3^6
                                    
5
1^2
                                    
3
1^3
                                    
2
1^4
                                    
5
2^3
                                    
1
2^4
                                    
6
help(^)
                                    
SyntaxError: invalid syntax
help(string)
                                    
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    help(string)
NameError: name 'string' is not defined
string
                                    
Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    string
NameError: name 'string' is not defined
import string
help(string)
Help on module string:

NAME
    string - A collection of string constants.

MODULE REFERENCE
    https://docs.python.org/3.11/library/string.html
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    Public module variables:
    
    whitespace -- a string containing all ASCII whitespace
    ascii_lowercase -- a string containing all ASCII lowercase letters
    ascii_uppercase -- a string containing all ASCII uppercase letters
    ascii_letters -- a string containing all ASCII letters
    digits -- a string containing all ASCII decimal digits
    hexdigits -- a string containing all ASCII hexadecimal digits
    octdigits -- a string containing all ASCII octal digits
    punctuation -- a string containing all ASCII punctuation characters
    printable -- a string containing all ASCII characters considered printable

CLASSES
    builtins.object
        Formatter
        Template
    
    class Formatter(builtins.object)
     |  Methods defined here:
     |  
     |  check_unused_args(self, used_args, args, kwargs)
     |  
     |  convert_field(self, value, conversion)
     |  
     |  format(self, format_string, /, *args, **kwargs)
     |  
     |  format_field(self, value, format_spec)
     |  
     |  get_field(self, field_name, args, kwargs)
     |      # given a field_name, find the object it references.
     |      #  field_name:   the field being looked up, e.g. "0.name"
     |      #                 or "lookup[3]"
     |      #  used_args:    a set of which args have been used
     |      #  args, kwargs: as passed in to vformat
     |  
     |  get_value(self, key, args, kwargs)
     |  
     |  parse(self, format_string)
     |      # returns an iterable that contains tuples of the form:
     |      # (literal_text, field_name, format_spec, conversion)
     |      # literal_text can be zero length
     |      # field_name can be None, in which case there's no
     |      #  object to format and output
     |      # if field_name is not None, it is looked up, formatted
     |      #  with format_spec and conversion and then used
     |  
     |  vformat(self, format_string, args, kwargs)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Template(builtins.object)
     |  Template(template)
     |  
     |  A string class for supporting $-substitutions.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, template)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  get_identifiers(self)
     |  
     |  is_valid(self)
     |  
     |  safe_substitute(self, mapping={}, /, **kws)
     |  
     |  substitute(self, mapping={}, /, **kws)
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  __init_subclass__() from builtins.type
     |      This method is called when a class is subclassed.
     |      
     |      The default implementation does nothing. It may be
     |      overridden to extend subclasses.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  braceidpattern = None
     |  
     |  delimiter = '$'
     |  
     |  flags = re.IGNORECASE
     |  
     |  idpattern = '(?a:[_a-z][_a-z0-9]*)'
     |  
     |  pattern = re.compile('\n            \\$(?:\n              ...identifie...

FUNCTIONS
    capwords(s, sep=None)
        capwords(s [,sep]) -> string
        
        Split the argument into words using split, capitalize each
        word using capitalize, and join the capitalized words using
        join.  If the optional second argument sep is absent or None,
        runs of whitespace characters are replaced by a single space
        and leading and trailing whitespace are removed, otherwise
        sep is used to split and join the words.

DATA
    __all__ = ['ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'cap...
    ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    hexdigits = '0123456789abcdefABCDEF'
    octdigits = '01234567'
    printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU...
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    whitespace = ' \t\n\r\x0b\x0c'

FILE
    /home/joelouma/anaconda3/lib/python3.11/string.py


>>> help(f_strings)
...                
Traceback (most recent call last):
  File "<pyshell#195>", line 1, in <module>
    help(f_strings)
NameError: name 'f_strings' is not defined. Did you mean: 'string'?
