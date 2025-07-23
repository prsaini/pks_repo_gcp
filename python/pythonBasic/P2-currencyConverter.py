
with open ('currencyData.txt') as file1:
    lines=file1.readlines()

dict2={}

for i in lines:
    line = i.split('\t')
    dict2[line[0]]=(line[1])

amt=int(input('Enter INR Amount to be converted: \n'))

[print(i) for i in dict2.keys()]
desCur=input('Select the desired currency from the above list: ')
newCurr=(amt)*float(dict2[desCur])
print(f'Converted value in {desCur} will be: {newCurr}')
