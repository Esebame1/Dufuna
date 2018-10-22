for i in range (1, 101):
    if i%2!=0:
        print(i)
        
for a in range (1,101):
    if a%2==0:
        print(a)


for p in range (2000,3301):
    if p%11==0:
        print(p)


def checkOccurence(lis,item):
    """(list,char) -> number
    """
    count=0
    for a in lis:
        if (a==item):
            count=count+1
    return count


def findPrimeNumbers(N,i=2):
    while(i<N):
        j=2
        while(j<=(i/j)):
            if not (i%j):
                continue
                j=j+1
            if (j>(i/j)):
                print(i)
                i=i+1
