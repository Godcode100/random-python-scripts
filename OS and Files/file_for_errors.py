#!usr/bin/env

def PrintErrors(Errors,depth=0):
    #if depth > 2:
    #    print("  &--"*(depth-2),end="")

    if depth > 1:
        print("  |"*(depth-1),end ="")
    
    if depth > 0:
        print("  +--",end="")

    print(Errors.__name__)
    for subclass in Errors.__subclasses__():
        PrintErrors(subclass,depth+1)
#PrintErrors(BaseException)