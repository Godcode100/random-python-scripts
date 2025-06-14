import os
from collections import Counter

counts = Counter()

for currdir,dirnames,filenames in os.walk('.'):
    for filename in filenames:
        firstpart,extension = os.path.splitext(filename)
        counts[extension]+=1
for extension,count in counts.items():
    print(f'{extension:8}{count}')
    print(counts.items())