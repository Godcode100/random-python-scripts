filename = 'test.txt'

print (f"Now we are going to erase content from {filename}")
print("If you dont want that hit CTRL -C")
print("If you do want that hit RETURN")
input("?")

print("opening the file...")
target = open(filename,'w')

print('Truncating the file .Goodbye!')
target.truncate()

print("Now we are going to ask you for 3 inputs")

line1=input("line1 input: ")
line2=input("line2 input: ")
line3=input("line3 input: ")

print("Time to write these to the file")

#formatter = '{}"\n" {}"\n" {}"\n"'
target.write('\n {}\n {}\n {}\n'.format(line1,line2,line3))
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("And finally we close it")
target.close()

txt = open(filename)
print(txt.read())