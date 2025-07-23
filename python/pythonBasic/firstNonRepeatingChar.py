s='abcdeabcdf'
l1=[]
for i in s:
    if i in l1:
        l1.remove(i)
    else:
        l1.append(i)
print(l1)