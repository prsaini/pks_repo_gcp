s='python is a very easy language'
l=s.split()
print(l)
print(len(l))
o=[]
for i in l:
    o.append(i[-1::-1])
print(o)



s='India'
op=''
i=len(s)-1

while i>=0:
    op=op+s[i]
    i-=1
print(op)