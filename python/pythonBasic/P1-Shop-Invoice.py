##Project to accept the item price and print a bill
sum = 0
item= 1
dict1={}
while(True):
    price = input('Enter the item price, Or press q to exit: ')
    if (price != 'q'):
        sum = sum + int(price)
        dict1[item]= int(price)
        item=item+1
        print (f'Total price so far is: {sum} Rs.')
    else:
        print (f'Your Total bill is {sum} Rs. Thanks for shopping with us ...')
        #print(dict1.keys(), dict1.values() for i in dict1)
        break


