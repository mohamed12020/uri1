a=int(input())
b=int(input())
if(a<b):
    li = []

    for i in range (a,1+b):
        if(i%13!=0):
            li.append(i)

elif(b<a):
    li = []

    for i in range (b,a+1):
        if(i%13!=0):
            li.append(i)

print(sum(li))