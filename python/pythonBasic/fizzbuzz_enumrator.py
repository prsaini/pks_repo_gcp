## Enumerate function provide the value with index in tuple
l1=[]
for i in range(5):
    l1.append(i)
print(l1)

l1=[]
for i,num in enumerate([1,2,3,4,5]):
    l1.append(i,num)
print(l1)



# l1=[3,5,15,17,20,21]
# for i,num in enumerate(l1):
#     if num%3==0 and num%5==0:
#         l1[i]='FizzBuzz'
#     elif num%3==0:
#         l1[i]='Fizz'
#     elif num%5==0:
#         l1[i]='Buzz'
# print(l1)