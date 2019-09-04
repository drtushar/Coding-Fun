# Enter your code here. Read input from STDIN. Print output to STDOUT
#7
#0 0 1 0 0 1 0
#o/p 4
#6
#0 0 0 1 0 0
#o/p 3
a = int(input())
input_arry = list(input().split())
jump = 0
i = 0
while i < a - 1:
    if i + 2 < a :
        if input_arry[i+2] != '1':
            i += 2
        else :
            i += 1
        jump += 1
    else:
        i += 1
        jump += 1        
print(jump,end="")                    
