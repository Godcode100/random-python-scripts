Python 3.11.4 (main, Jul  5 2023, 14:15:25) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> cmd = 'open -a "Google Chrome"'
>>> cmd.split()
['open', '-a', '"Google', 'Chrome"']
>>> import shlex
>>> shlex.split(cmd)
['open', '-a', 'Google Chrome']
>>> import webbrowser
>>> url = 'http://127.0.0.1:8000/'
>>> webbrowser.open(url)
True
