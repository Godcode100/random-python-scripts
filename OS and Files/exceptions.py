#!usr/bin/env

def PrintPythonExceptions(ExceptionsClass,level=0):
    if level>1:
        print("  |"*(level-1),end="")

    if level >0:
        print("  +---",end='')
    
    print(ExceptionsClass.__name__)
    for subclass in ExceptionsClass.__subclasses__():
        print(subclass,level+1)
    
if __name__ =="__main__":
    PrintPythonExceptions(Exception)