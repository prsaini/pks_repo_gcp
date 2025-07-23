input1=input('input a string: ')
l1=list(input1)
l2=[]
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]==l1[j] and l1[i] not in l2:
            l2.append(l1[i])
print(l2)