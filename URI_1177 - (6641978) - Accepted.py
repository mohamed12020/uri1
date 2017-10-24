li=[]
li2=[]
n=-1

a=int(input())

if(2<=a<=50):
 for i in range(1000//a):
   li2.extend(li)
   for i in range(a):
    li.append(i)
 for num  in li2:
     n += 1
     print("N[",n,"] = ",num,sep="")
     if(n==999):
       break
