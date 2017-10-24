a,b,c=map(float,input().split())
if (a+b>c)and(c+b>a) and(a+c>b):
    p=a+b+c
    print("Perimetro = {:.1f}".format(p))
else:
    r=(((a+b)/2)*c)
    print("Area = {:.1f}".format(r))