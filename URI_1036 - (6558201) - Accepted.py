a,b,c=map(float,input().split())
d=((b*b)-(4*a*c))

if(a!=0)and (d>0):
    r1 = ((-b + (d ** .5)) / (2 * a))
    r2 = ((-b - (d ** .5)) / (2 * a))
    print ("R1 = {:.5f}".format(r1))
    print ("R2 = {:.5f}".format(r2))
else:
    print("Impossivel calcular")
