Python 3.11.4 (main, Jul  5 2023, 14:15:25) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
class SecretAgent:
    _codeword = None
    def __init__(self,codename):
        self.codename = codename
        self._secrets = []
    def remember(self,secret):
        self._secrets.append(secret)
    def __del__(self):
        print(f"Agent{self.codename} has been disavowed")
    @classmethod
    def inform(cls,codeword):
        cls._codeword = codeword

        


================= RESTART: /home/joelouma/Desktop/using_ord.py =================
Traceback (most recent call last):
  File "/home/joelouma/Desktop/using_ord.py", line 1, in <module>
    code = agent
NameError: name 'agent' is not defined. Did you mean: 'anext'?

================= RESTART: /home/joelouma/Desktop/using_ord.py =================
<generator object <genexpr> at 0x7f2044cd74c0>

================= RESTART: /home/joelouma/Desktop/using_ord.py =================
<generator object <genexpr> at 0x7feaf94d74c0>
Traceback (most recent call last):
  File "/home/joelouma/Desktop/using_ord.py", line 3, in <module>
    print(ord (x) for x in agent)
NameError: name 'agent' is not defined. Did you mean: 'anext'?

================= RESTART: /home/joelouma/Desktop/using_ord.py =================
<generator object <genexpr> at 0x7fd551ddb4c0>
<generator object <genexpr> at 0x7fd551ddb4c0>

================= RESTART: /home/joelouma/Desktop/using_ord.py =================
<generator object <genexpr> at 0x7f4ed02d74c0>
<generator object <genexpr> at 0x7f4ed02d74c0>

================= RESTART: /home/joelouma/Desktop/using_ord.py =================
<generator object <genexpr> at 0x7efc239db4c0>
<generator object <genexpr> at 0x7efc239db4c0>

================= RESTART: /home/joelouma/Desktop/using_ord.py =================
<generator object <genexpr> at 0x7f3ef63d74c0>
<generator object <genexpr> at 0x7f3ef63d74c0>
527
help(ord())
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    help(ord())
TypeError: ord() takes exactly one argument (0 given)
help(ord)
Help on built-in function ord in module builtins:

ord(c, /)
    Return the Unicode code point for a one-character string.

class SecretAgent:
    _codeword = None
    def __init__(self,codename):
        self.codename = codename
        self._secrets = []
    def remember(self,secret):
        self._secrets.append(secret)
    def __del__(self):
        print(f"Agent{self.codename} has been disavowed")
    @classmethod
    def inform(cls,codeword):
        cls._codeword = codeword
    @staticmethod
    def inquire(question):
        print("I know nothing")
    @classmethod
    def _encrypt(cls,message,*,decrypt = False):
        code = sum(ord(c) for c in codeword)
        if decrypt:
            code = -code
        return ''.join(chr(ord(m) + code) for m in message)

    

================= RESTART: /home/joelouma/Desktop/using_ord.py =================
<generator object <genexpr> at 0x7ff6251db4c0>
<generator object <genexpr> at 0x7ff6251db4c0>
527
<generator object <genexpr> at 0x7ff62414e5c0>

================= RESTART: /home/joelouma/Desktop/using_ord.py =================
<generator object <genexpr> at 0x7fde766d74c0>
<generator object <genexpr> at 0x7fde766d74c0>
527
Traceback (most recent call last):
  File "/home/joelouma/Desktop/using_ord.py", line 5, in <module>
    print(chr(ord(x) for x in 'agent'))
TypeError: 'generator' object cannot be interpreted as an integer

================= RESTART: /home/joelouma/Desktop/using_ord.py =================
<generator object <genexpr> at 0x7f9a0b9d74c0>
<generator object <genexpr> at 0x7f9a0b9d74c0>
527
<generator object <genexpr> at 0x7f9a0a9225c0>

================= RESTART: /home/joelouma/Desktop/using_ord.py =================
<generator object <genexpr> at 0x7f03970d74c0>
<generator object <genexpr> at 0x7f03970d74c0>
527
<generator object <genexpr> at 0x7f039609e6b0>
<generator object <genexpr> at 0x7f039609e6b0>

================= RESTART: /home/joelouma/Desktop/using_ord.py =================
<generator object <genexpr> at 0x7f7b4a0d74c0>
<generator object <genexpr> at 0x7f7b4a0d74c0>
527
<generator object <genexpr> at 0x7f7b48ff26b0>
<generator object <genexpr> at 0x7f7b48ff26b0>

================= RESTART: /home/joelouma/Desktop/using_ord.py =================
<generator object <genexpr> at 0x7fe3879db4c0>
<generator object <genexpr> at 0x7fe3879db4c0>
527
<generator object <genexpr> at 0x7fe38690e6b0>
<generator object <genexpr> at 0x7fe38690e6b0>
109

================= RESTART: /home/joelouma/Desktop/using_ord.py =================
<generator object <genexpr> at 0x7f338e5db4c0>
<generator object <genexpr> at 0x7f338e5db4c0>
527
<generator object <genexpr> at 0x7f338d59a6b0>
<generator object <genexpr> at 0x7f338d59a6b0>
109
101
115
115
115
97
103
101

================= RESTART: /home/joelouma/Desktop/using_ord.py =================
<generator object <genexpr> at 0x7fc53fcd74c0>
<generator object <genexpr> at 0x7fc53fcd74c0>
527
<generator object <genexpr> at 0x7fc53ec566b0>
<generator object <genexpr> at 0x7fc53ec566b0>
97
103
101
110
116

================= RESTART: /home/joelouma/Desktop/using_ord.py =================
<generator object <genexpr> at 0x7fc671ed74c0>
<generator object <genexpr> at 0x7fc671ed74c0>
527
<generator object <genexpr> at 0x7fc670eb66b0>
<generator object <genexpr> at 0x7fc670eb66b0>
97
103
101
110
116

================= RESTART: /home/joelouma/Desktop/using_ord.py =================
<generator object <genexpr> at 0x7fa7e67db4c0>
<generator object <genexpr> at 0x7fa7e67db4c0>
527
<generator object <genexpr> at 0x7fa7e56e26b0>
<generator object <genexpr> at 0x7fa7e56e26b0>
97
103
101
110
116
n

================= RESTART: /home/joelouma/Desktop/using_ord.py =================
<generator object <genexpr> at 0x7f6afe8d74c0>
<generator object <genexpr> at 0x7f6afe8d74c0>
527
<generator object <genexpr> at 0x7f6afd83a6b0>
<generator object <genexpr> at 0x7f6afd83a6b0>
97
103
101
110
116
n
Traceback (most recent call last):
  File "/home/joelouma/Desktop/using_ord.py", line 14, in <module>
    print(ord('message'))
TypeError: ord() expected a character, but string of length 7 found

================= RESTART: /home/joelouma/Desktop/using_ord.py =================
<generator object <genexpr> at 0x7f61db3db4c0>
<generator object <genexpr> at 0x7f61db3db4c0>
527
<generator object <genexpr> at 0x7f61da2d66b0>
<generator object <genexpr> at 0x7f61da2d66b0>
97
103
101
110
116
n
109
101
115
115
97
103
101

================= RESTART: /home/joelouma/Desktop/using_ord.py =================
<generator object <genexpr> at 0x7fac641db4c0>
<generator object <genexpr> at 0x7fac641db4c0>
527
<generator object <genexpr> at 0x7fac6313a6b0>
<generator object <genexpr> at 0x7fac6313a6b0>
97
103
101
110
116
n
109
101
115
115
97
103
101
527

================= RESTART: /home/joelouma/Desktop/using_ord.py =================
<generator object <genexpr> at 0x7fb2e7bdb4c0>
<generator object <genexpr> at 0x7fb2e7bdb4c0>
527
<generator object <genexpr> at 0x7fb2e6b1e6b0>
<generator object <genexpr> at 0x7fb2e6b1e6b0>
97
103
101
110
116
n
109
101
115
115
97
103
101
527
636
628
642
642
624
630
628

================= RESTART: /home/joelouma/Desktop/using_ord.py =================
<generator object <genexpr> at 0x7f33856d74c0>
<generator object <genexpr> at 0x7f33856d74c0>
527
<generator object <genexpr> at 0x7f33845f66b0>
<generator object <genexpr> at 0x7f33845f66b0>
97
103
101
110
116
n
109
101
115
115
97
103
101
527
636
ɼ
628
ɴ
642
ʂ
642
ʂ
624
ɰ
630
ɶ
628
ɴ
class SecretAgent:
    _codeword = None
    def __init__(self,codename):
        self.codename = codename
        self._secrets = []
    def remember(self,secret):
        self._secrets.append(secret)
    def __del__(self):
        print(f"Agent{self.codename} has been disavowed")
    @classmethod
    def inform(cls,codeword):
        cls._codeword = codeword
    @staticmethod
    def inquire(question):
        print("I know nothing")
    @classmethod
    def _encrypt(cls,message,*,decrypt = False):
        code = sum(ord(c) for c in codeword)
        if decrypt:
            code = -code
        return ''.join(chr(ord(m) + code) for m in message)
    def _getsecret(self):
        self._secrets[-1] if self._secrets else None
    def _setsecret(self,value):
        self._secrets.append(self._encrypt(value))
    def _delsecret(self):
        self._secrets = []
    secret = property(fget=_getsecret,fset=_setsecret,fdel=_delsecret)

    
mouse = SecretAgent("mickey")
print(mouse.secret)
None
mouse.secret = "plot 45 Colvile Street"
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    mouse.secret = "plot 45 Colvile Street"
  File "<pyshell#45>", line 25, in _setsecret
    self._secrets.append(self._encrypt(value))
  File "<pyshell#45>", line 18, in _encrypt
    code = sum(ord(c) for c in codeword)
NameError: name 'codeword' is not defined
mouse.inform("Permeaso")
mouse.secret = "Plot 45 Colville Street"
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    mouse.secret = "Plot 45 Colville Street"
  File "<pyshell#45>", line 25, in _setsecret
    self._secrets.append(self._encrypt(value))
  File "<pyshell#45>", line 18, in _encrypt
    code = sum(ord(c) for c in codeword)
NameError: name 'codeword' is not defined
mouse = SecretAgent("mickey")
mouse.inform("Permeaso")
print(mouse.secret)
None
mouse.secret = "Plot 45 Colville Street"
Agentmickey has been disavowed
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    mouse.secret = "Plot 45 Colville Street"
  File "<pyshell#45>", line 25, in _setsecret
    self._secrets.append(self._encrypt(value))
  File "<pyshell#45>", line 18, in _encrypt
    code = sum(ord(c) for c in codeword)
NameError: name 'codeword' is not defined
mouse = SecretAgent("mickey")
mouse.inform("Permeaso")
print(mouse.secret)
None
class SecretAgent:
    _codeword = None
    def __init__(self,codename):
        self.codename = codename
        self._secrets = []
    def remember(self,secret):
        self._secrets.append(secret)
    def __del__(self):
        print(f"Agent{self.codename} has been disavowed")
    @classmethod
    def inform(cls,codeword):
        cls._codeword = codeword
    @staticmethod
    def inquire(question):
        print("I know nothing")
    @classmethod
    def _encrypt(cls,message,*,decrypt = False):
        code = sum(ord(c) for c in _codeword)
        if decrypt:
            code = -code
        return ''.join(chr(ord(m) + code) for m in message)
    def _getsecret(self):
        self._secrets[-1] if self._secrets else None
    def _setsecret(self,value):
        self._secrets.append(self._encrypt(value))
    def _delsecret(self):
        self._secrets = []
    secret = property(fget=_getsecret,fset=_setsecret,fdel=_delsecret)

    
mouse = SecretAgent("mickey")mouse.inform("Permeaso")
SyntaxError: invalid syntax
mouse = SecretAgent("mickey")
Agentmickey has been disavowed
mouse = SecretAgent("mickey")
Agentmickey has been disavowed
mouse = SecretAgent("mick")
Agentmickey has been disavowed
mouse = SecretAgent("Joe")
Agentmick has been disavowed
mouse.inform("Jesus Christ")
print(mouse.secret)
None
mouse.secret = "plot 45 Colville Street"
Agentmickey has been disavowed
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    mouse.secret = "plot 45 Colville Street"
  File "<pyshell#59>", line 25, in _setsecret
    self._secrets.append(self._encrypt(value))
  File "<pyshell#59>", line 18, in _encrypt
    code = sum(ord(c) for c in _codeword)
NameError: name '_codeword' is not defined
class SecretAgent:
    _codeword = None
    def __init__(self,codename):
        self.codename = codename
        self._secrets = []
    def remember(self,secret):
        self._secrets.append(secret)
    def __del__(self):
        print(f"Agent{self.codename} has been disavowed")
    @classmethod
    def inform(cls,codeword):
        cls._codeword = codeword
    @staticmethod
    def inquire(question):
        print("I know nothing")
    @classmethod
    def _encrypt(cls,message,*,decrypt = False):
        code = sum(ord(c) for c in cls._codeword)
        if decrypt:
            code = -code
        return ''.join(chr(ord(m) + code) for m in message)
    def _getsecret(self):
        self._secrets[-1] if self._secrets else None
    def _setsecret(self,value):
        self._secrets.append(self._encrypt(value))
    def _delsecret(self):
        self._secrets = []
    secret = property(fget=_getsecret,fset=_setsecret,fdel=_delsecret)

    
mouse = SecretAgent("joe")
mouse.inform("Jesus Christ")
print(mouse.secret)
None
mouse.secret =
SyntaxError: incomplete input
mouse.secret ="plot 45 Colville Street"
print(mouse.secret)
None
print(mouse._secrets)
['ԇԃԆԋҷӋӌҷӚԆԃԍԀԃԃӼҷӪԋԉӼӼԋ']
print(mouse.secret)
None
mouse.secret ="plot 45 Colville Street"mouse.secret = "5555-2345"
SyntaxError: invalid syntax
mouse.secret = "5555-2345"
print(mouse.secret)
None
print(mouse._secrets)
['ԇԃԆԋҷӋӌҷӚԆԃԍԀԃԃӼҷӪԋԉӼӼԋ', 'ӌӌӌӌӄӉӊӋӌ']
class SecretAgent:
    _codeword = None
    def __init__(self,codename):
        self.codename = codename
        self._secrets = []
    def remember(self,secret):
...         self._secrets.append(secret)
...     def __del__(self):
...         print(f"Agent{self.codename} has been disavowed")
...     @classmethod
...     def inform(cls,codeword):
...         cls._codeword = codeword
...     @staticmethod
...     def inquire(question):
...         print("I know nothing")
...     @classmethod
...     def _encrypt(cls,message,*,decrypt = False):
...         code = sum(ord(c) for c in cls._codeword)
...         if decrypt:
...             code = -code
...         return ''.join(chr(ord(m) + code) for m in message)
...     def _getsecret(self):
...         return self._secrets[-1] if self._secrets else None
...     def _setsecret(self,value):
...         self._secrets.append(self._encrypt(value))
...     def _delsecret(self):
...         self._secrets = []
...     secret = property(fget=_getsecret,fset=_setsecret,fdel=_delsecret)
... 
...     
>>> mouse = SecretAgent("joe")
Agentjoe has been disavowed
>>> mouse.inform("Jesus Christ")
>>> print(mouse.secret)
None
>>> mouse.secret ="plot 45 Colville Street"
>>> print(mouse.secret)
ԇԃԆԋҷӋӌҷӚԆԃԍԀԃԃӼҷӪԋԉӼӼԋ
>>> print(mouse._secrets)
['ԇԃԆԋҷӋӌҷӚԆԃԍԀԃԃӼҷӪԋԉӼӼԋ']
>>> mouse.secret = "5555-2345"
>>> print(mouse.secret)
ӌӌӌӌӄӉӊӋӌ
>>> print(mouse._secrets)
['ԇԃԆԋҷӋӌҷӚԆԃԍԀԃԃӼҷӪԋԉӼӼԋ', 'ӌӌӌӌӄӉӊӋӌ']
