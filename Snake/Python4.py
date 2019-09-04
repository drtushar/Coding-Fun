test=int(input())
for t in range(test):
    arrlen = int(input())
    arr = list(map(int, input().split()))
    result = []
    xor = 0
    for i in arr:
        xor = xor ^ i
        result.append(xor)
    print(result)




































# # # Compound Interest = P(1 + R/100)r
# #
# # P = float(raw_input("Enter Principle : "))
# # R = float(raw_input("Enter Rate : "))
# # # T = float(raw_input("Enter Time : "))
# # #
# # # P = P * pow(1 + R/100,T)
# # # print("The Compound Interest is {0}".format(P))
# from __future__ import print_function
# # # a = 5
# # # b = 3
# # # c = float(a)/b
# # # s = "abcdefgh"
# # print("{:.3f} is {:d} ans {:10.5s}".format(c,a,s))
# # print("{}".format(ord('a')))
# # l = list(map(float,raw_input().split()))
# # print(l,end=" lol")
#
# i = 10
# bin(1,1)
# print(hex(i))
# def prime(no):
#     i=2
#     while i*i <= no:
#         if no%i==0:
#             return False
#         i+=1
#     return True
#
# n,m = map(int, raw_input().split())
# if n%2==0:
#     n+=1
# ans = 0
# for i in range(n,m+1,2):
#     if prime(i):
#         print(i,end=" ")
#         ans += 1
# print(ans/2)
