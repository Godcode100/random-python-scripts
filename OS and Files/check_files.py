import os
for root,directories,files in os.walk(".",topdown=False):
    for file in files:
        print("[+]" , os.path.join(root,file))
        for directory in directories:
            print("[++]",directory)