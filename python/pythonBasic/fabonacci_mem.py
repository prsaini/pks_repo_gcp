## Fabonacci series with Memoization

fab_hist={}

def fab(num):

    if num in fab_hist:
        return fab_hist[num]

    if num==1 or num==2:
        value=1
    else:
        value=fab(num-1)+fab(num-2)

    ## Cache the value and return it
    fab_hist[num]=value
    return value


for i in range(1,50):
    print(i,' : ',fab(i))