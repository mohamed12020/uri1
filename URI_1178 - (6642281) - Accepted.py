li=[]
n=0
c=-1
a=float(input())
for i in range(100):
    li.insert(n,a)
    a/=2
    n+=1
for num in li:
    c+=1
    print("N[",c,"] = {:.4f}".format(num),sep="")