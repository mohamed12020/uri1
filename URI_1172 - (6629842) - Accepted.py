n=-1
li = [int(input()) for i in range(10)]

for i in range(10):
    n+=1
    if(li[i]<0):
        li[i]=1
    if(li[i]==0):
        li[i]=1
    print("X[",n,"]"," = ",li[i],sep="")