# #Program to add 2 numbers
# number1 = raw_input("Enter 1st number : ");
# number2 = raw_input("Enter 2nd number : ");
#
# sum = int(number1) + int(number2)
#
# print("The Sum of {0} and {1} is {2}".format(number1,number2,sum))

#PYTHON 2.7 :
#raw_input takes input as it is while input() takes string input and eval() on it
#ie evaluate the string ie try to solve it like expression and returns result.

#Python 3.x :
# raw_input is renamed as input() so now input() returns exact string.
# Old input() is removed.
#
# noofholes = int(input())
# HolesDir = list(map(int, input().split()))
# noofballs = int(input())
# balldir = list(map(int, input().split()))
#
# holesplots = []
# m = {}
# for i in range(1,noofholes+1):
#     holesplots.append(i)
#     m[str(HolesDir[i-1])] = i
# print(m)
# ans = []
# for i in balldir:
#     t = 0
#     for j in range(0,len(holesplots)):
#         if holesplots[noofholes-1-j] != 0:
#             if i <= HolesDir[noofholes-1-j]:
#                 print("i = ",i,"holeDir = ",HolesDir[noofholes-1-j],"holesplots[] = ",holesplots[noofholes-1-j])
#                 t = m[str(HolesDir[noofholes-1-j])]
#                 ans.append(t)
#                 holesplots[noofholes-1-j] -= 1
#     if t == 0:
#         ans.append(t)
#
# print(ans)

noofholes = int(input())
HolesDir = list(map(int, input().split()))
noofballs = int(input())
balldir = list(map(int, input().split()))

holesplots = []
m = {}
for i in range(1,noofholes+1):
    holesplots.append(i)
    m[str(HolesDir[i-1])] = i
ans = []
for i in balldir:
    t = 0
    for j in range(0,len(holesplots)):
        if holesplots[noofholes-1-j] != 0:
            if i <= HolesDir[noofholes-1-j]:
                t = m[str(HolesDir[noofholes-1-j])]
                ans.append(t)
                holesplots[noofholes-1-j] -= 1
                break
    if t == 0:
        ans.append(t)


for i in range(0,len(ans)):
  if i != len(ans)-1:
  	print(ans[i],end=" ")
  else:
    print(ans[i])

# import math
# n = int(input())
# x = []
# y = []
# for i in range(0,n):
#   a = list(map(int,input().split()))
#   a[0] = (a[0] + a[2])/2
#   a[1] = (a[1] + a[3])/2
#   x.append(a[0])
#   y.append(a[1])
# ipp = list(map(int, input().split()))
# for i in range(0,n):
#   x[i] = math.sqrt((x[i] - ipp[0])*(x[i] - ipp[0]) + (y[i] - ipp[1])*(y[i] - ipp[1]))
#
# for i in range(0,n):
#     y[i] = x[i]
#
# y.sort()
# for i in y:
#   print(x.index(i)+1,end=" ")

# n = int(input())
# x = []
# y = []
# for i in range(0,n):
#   a = list(map(int,input().split()))
#   a[0] = (a[0] + a[2])/2
#   a[1] = (a[1] + a[3])/2
#   x.append(a[0])
#   y.append(a[1])
# ipp = list(map(int, input().split()))
#
#
# for i in range(0,n):
#   x[i] = abs(abs(x[i] - ipp[0]) + abs(y[i] - ipp[1]))
#
# y = []
# for i in range(0,n):
#   y.append(x[i])
# y.sort()
# print(x.index(y[0])+1,end="")
# for i in range(1,n):
#   print("",x.index(y[i])+1,end="")

n = int(input())
ship = []
for i in range(0,n):
  a = list(map(int,input().split()))
  ship.append(a)
ipp = list(map(int, input().split()))
l = []
y = []
j = 1
for i in ship:
  l.append(min(abs(i[0]-ipp[0]) + abs(i[1]-ipp[1]),abs(i[2]-ipp[0]) + abs(i[3]-ipp[1]),abs(i[0]-ipp[0]) + abs(i[3]-ipp[1]),abs(i[2]-ipp[0]) + abs(i[1]-ipp[1])))
  y.append(j)
  j += 1

l,y = zip(*sorted(zip(l,y)))
print(y[0],end="")
for i in range(1,n):
    print("",y[i],end="")
