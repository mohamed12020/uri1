a=int(input())
list1=[]
for num in range(1,a+1):
    if(num%2==0):
     c=num**2
     print(num,"^2 = ",c,sep="")