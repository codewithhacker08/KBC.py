def fibonacci(n):
  if(n==0 or n==1):
    return 1
  else:
      return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Please enter the number which you want to calculate :"))
print("Fibonacci of",n,"is :",fibonacci(n))
