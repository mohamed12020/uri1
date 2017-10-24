a=int(input())
b=[int(input()) for i in range(a)]


for num in b:

  if (num > 1):

    for i in range(2 , num):
        if (num % i) == 0:
            print(num , "nao eh primo")

            break
    else:
        print(num , "eh primo")

  else:
    print(num , "nao eh primo")