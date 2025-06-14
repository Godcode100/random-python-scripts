code = 'agent'
print(ord(c)for c in code)
print(ord (x) for x in 'agent')
print(sum(ord(x) for x in 'agent'))
print(chr(ord(x)) for x in 'agent')
mem = sum(ord(c) for c in 'agent')
print(chr(ord(m) + mem) for m in 'message')
print(ord('a'))
print(ord('g'))
print(ord('e'))
print(ord('n'))
print(ord('t'))
print(chr(110))
for x in 'message':
    print(ord(x))
print(mem)
for x in 'message':
    print(ord(x)+ mem)
    print(chr(ord(x) + mem))
