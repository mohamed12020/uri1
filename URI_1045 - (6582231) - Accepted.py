a,b,c=map(float,input().split())
list1=[a,b,c]
list1.sort()
x=list1[2]
y=list1[1]
z=list1[0]

if(x < (y + z)):

   if((x**2)==(y**2)+(z**2)) :
    print("TRIANGULO RETANGULO")
   if((x**2)>(y**2)+(z**2)):
    print("TRIANGULO OBTUSANGULO")
   if ((x**2)<((y**2)+(z**2))):
    print("TRIANGULO ACUTANGULO")
   if(x==y==z):
    print("TRIANGULO EQUILATERO")
   if((x==y) or (x==z) or (z==y)) and ((x+y+z)!=(3*x)):
    print("TRIANGULO ISOSCELES")
else:
    print("NAO FORMA TRIANGULO")
