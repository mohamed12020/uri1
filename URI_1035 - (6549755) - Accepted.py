a,b,c,d=map(int,input().split())
s1=c+d
s2=a+b
if (b>c) and (d>a) and (s1>s2) and (c>0) and (d>0) and (a%2<= 0) :
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
