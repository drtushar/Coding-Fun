# # Python code to print Prime numbers in an interval :
# start = 11
# end = 25
#
# for i in range(start,end+1):
#     if i > 1:
#         flag = 1
#         for j in range(2,int(pow(i,0.5)+1)):
#             if i%j == 0:
#                 flag = 0
#                 break
#         if flag == 1:
#             print(i)
# t = int(input())
# for test in range(0,t):
#     arrayLen = int(input())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#     max = 0
#     for i in range(0,arrayLen):
#         tus = 2*a[i] - b[i]
#         if tus > max:
#             max = tus
#     print(max)

# t = int(input())
# for test in range(0,t):
#     n,k = map(int, input().split())
#     Result = n/k
#     r = [0]*k
#     i = 0
#     flag = 1
#     while n!=0:
#         r[i] += k
#         n -= k
#         if r[i] > Result:
#             flag = 2
#             print("YES")
#             break
#         i = (i+1)%k
#     if flag == 1:
#         print("NO")

t = int(input())
for test in range(0,t):
    arrayLen = int(input())
    arr = list(map(int,input().split()))
    xor = 0
    Result = [0]*arrayLen
    ans = 0
    for i in range(arrayLen):
        xor = xor ^ arr[i]
        Result[i] = xor
        if xor == 0:
            ans += i
    print(Result)        
    for i in range(0,arrayLen-1):
        for j in range(i+1,arrayLen):
            if Result[j] ^ Result[i] == 0:
                ans += j-i-1
    print(ans)


# t = int(input())
# for test in range(0,t):
#     s = list(input())
#     i = 0
#     sum = 0
#     lenstr = len(s)
#     while i < lenstr:
#         if s[i] == '1':
#             s[i] = 'B'
#             sum += 1
#             if i == 0:
#                 if s[i+1] == '1':
#                     s[i+1] = '0'
#                 elif s[i+1] == '0':
#                     s[i+1] = '1'
#             elif i == lenstr -1:
#                 if s[i-1] == '1':
#                     s[i-1] = '0'
#                 elif s[i-1] == '0':
#                     s[i-1] = '1'
#                     i -= 2
#             else:
#                 if s[i+1] == '1':
#                     s[i+1] = '0'
#                 elif s[i+1] == '0':
#                     s[i+1] = '1'
#                 if s[i-1] == '1':
#                     s[i-1] = '0'
#                 elif s[i-1] == '0':
#                     s[i-1] = '1'
#                     i -= 2
#         i += 1
#     if sum == lenstr:
#         print("WIN")
#     else:
#         print("LOSE")
# t = int(input())
# for test in range(0,t):
#     arrayLen = int(input())
#     C = list(map(int,input().split()))
#     H = list(map(int,input().split()))
#     Result = [0]*arrayLen
#     i = 1
#     sum = 0
#     for k in H:
#         sum += k
#     for ci in C:
#          low = i-ci
#          high = i+ci
#          if low < 1:
#              low = 1
#          if high > arrayLen:
#              high = arrayLen
#          sum -= high - low + 1
#          # for j in range(low-1,high):
#          #     Result[j] += 1
#          i += 1
#     if sum == 0:
#         print("YES")
#     else:
#         print("NO")
    # print(Result)
    # m = {}
    # for k in Result:
    #     if k in m:
    #         m[k] += 1
    #     else:
    #         m[k] = 1
    # for k in H:
    #     if k in m:
    #         m[k] -= 1
    # flag = 1
    # for k in m:
    #     if m[k] != 0:
    #         flag = 2
    #         break
    # if flag == 1:
    #     print("YES")
    # else:
    #     print("NO")
