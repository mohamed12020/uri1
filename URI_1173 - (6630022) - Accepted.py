a=int(input())
list1=[]
n=-1
if(a<50):
 for i in range(10):
    n+=1
    list1.append(a)
    a*=2
    print("N[",n,"]"," = ",list1[i],sep="")