import os

file_count =0
for currentdir,directories,filenames in os.walk("."):
    file_count +=len(filenames)
print ("The number of files", file_count)