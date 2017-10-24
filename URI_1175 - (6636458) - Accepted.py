n=-1
b=[int(input()) for i in range(20)]
b.reverse()
for i in range(20):
    n+=1
    print("N[",n,"] = ",b[i],sep="")