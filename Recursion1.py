
#Author : Naina Chaturvedi
#Problem Statement : Fibonnaci numbers


def Fib(n):
    sum1=0
    if n < 0:
        return -1
    elif n==0:
          return 1
    else :
          #while n>=1:
           return (Fib(n-1)+ Fib(n-2))

if __name__ == '__main__':
 no= 10
 for i in range(no):
  fibResult=Fib(no)
 print("The fibonacci result is ",fibResult)

