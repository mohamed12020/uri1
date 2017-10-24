a=int(input())
bo = [int(input()) for i in range(a)]
s=0
n=0
for num in bo :
    if(10<=num<=20):
        s+=1
    else:
        n+=1
print(s,"in")
print(n,"out")