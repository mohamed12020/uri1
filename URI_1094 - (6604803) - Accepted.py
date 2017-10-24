a=int(input())
list1=[]
list2=[]
list3=[]
for i in range(a):
    x , y = input().split()
    if (y== "C" ):
     list1.append(x)

    elif(y=="R"):
     list2.append(x)
    elif(y=="S"):
     list3.append(x)
b=list(map(int, list1))
c=list(map(int, list2))
d=list(map(int, list3))
e=sum(b)+sum(c)+sum(d)

print("Total:",e,"cobaias")
print("Total de coelhos:",sum(b))
print("Total de ratos:",sum(c))
print("Total de sapos:",sum(d))
print("Percentual de coelhos: {:.2f}".format((sum(b)/e)*100),"%")
print("Percentual de ratos: {:.2f}".format((sum(c)/e)*100),"%")
print("Percentual de sapos: {:.2f}".format((sum(d)/e)*100),"%")
