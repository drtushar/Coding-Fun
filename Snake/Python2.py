# Python 2.7 code to find factorial recusively :

def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n-1)

n = int(raw_input("Enter no to calculate factorial : "))
print("The factorial of {0} is {1}".format(n,factorial(n)))
