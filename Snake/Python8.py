#Python 2.X code for fibonacci using Dp with memory optimization

def fib(n):
    a = 0
    b = 1
    if n<0:
        print("Incorrect")
    elif n==0:
        return 0
    elif n==1:
        return 0
    else:
        for i in range(2,n):
            c = a+b
            a = b;
            b = c
        return b

print(fib(9))  
