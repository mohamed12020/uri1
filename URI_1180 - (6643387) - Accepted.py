a=int(input())
b=[ int(i) for i in  input().split() ]
c=min(b)
print("Menor valor:",c)
print("Posicao:",b.index(c))
