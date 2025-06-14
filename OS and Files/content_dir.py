import os
pwd = os.getcwd()
#listdir = os.listdir(pwd)
#listdir =os.walk('/home/joelouma')
listdir = os.listdir('/home/joelouma/Downloads')
for directory in listdir:
    print(directory)