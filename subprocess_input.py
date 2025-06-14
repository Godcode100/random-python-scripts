#!usr/bin/python3
import subprocess
import sys

#Sometimes programs expect to be passed data through the standard input, stdin arg. The input argument allows you to oass data to the
#thread's standard input

result = subprocess.run([sys.executable,"-c","import sys; print(sys.stdin.read())"],input=b'python,core')