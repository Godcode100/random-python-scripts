from sys import argv
from os.path import exists

from_file = 'test.txt'
to_file = 'new_test.txt'


in_file = open(from_file)
indata = in_file.read()

print(f"The file is {len(indata)} bytes long")
print(f"Does the output file exist?{exists(to_file)}")
print("Hit Return to continue CTRL-C to exist")
input("%")

out_file = open(to_file,'w')
out_file.write(indata)

print("All done")
in_file.close()
out_file.close()