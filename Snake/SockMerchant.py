# Enter your code here. Read input from STDIN. Print output to STDOUT
# 9
# 10 20 20 10 10 30 50 10 20
no_of_socks = int(input())
input_arry = list(input().split())
d = {}
pair = 0
for i in input_arry:
    a = int(i)
    if a not in d :
        d[a] = 1
    else:
        if d[a] + 1 == 2:
            pair += 1
            d[a] = 0
        else:
            d[a] = 1    
print(pair,end="")

