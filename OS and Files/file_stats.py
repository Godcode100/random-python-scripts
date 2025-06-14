import os
import time

file= "scan.py"
st = os.stat(file)
print(st)
mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
print ("-size", size, "bytes")
print("-created at",time.ctime(ctime))
print("Modified",time.ctime(mtime))
print("Last Accesed",time.ctime(atime))
print("User",gid,uid)
print("Mode",oct(mode))