a=int(input())
n=1
listn=[]
for i in range(0,a):
    a,b,c=map(float,input().split())
    listn=[a,b,c]
    n+=1
    avg=(((a*2)+(b*3)+(c*5))/10)
    print("{:.1f}".format(avg))