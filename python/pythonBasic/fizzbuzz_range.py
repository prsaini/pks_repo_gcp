num=2
l1=[3,5,15,17,20,21]

for i in range(1,num):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)

for i in range(len(l1)):
    if l1[i]%3==0 and l1[i]%5==0:
        l1[i]='FizzBuzz'
    elif l1[i]%3==0:
        l1[i]='Fizz'
    elif l1[i]%5==0:
        l1[i]='Buzz'
print(l1)