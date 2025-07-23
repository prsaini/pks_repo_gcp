from collections import Counter
input1=input('input a string: ')
# input1='ABCABCANC'
output1=[]
l1=list(input1) # converting to list
l2=Counter(l1)  # Counting letters and converting to dictionary

for k in l2.keys():
    print(k,l2[k])

for v in l2.values():
    print(v)

for k,v in l2.items():
    print(k,v)

for k,v in l2.items():
    if v>1:
        output1.append(k)
print(input1)
print(output1)
