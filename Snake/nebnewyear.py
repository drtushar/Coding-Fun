def main():
     test = int(input())
     for t in range(0,test):
         n = int(input())
         neb = list(map(int , input().split()))
         sortneb = []
         sortneb.extend(neb)
         sortneb.sort(reverse=True)
         kuch = []
         kuch.extend(neb)
         indexesofsorted = []
         notallowed = []
         for i in sortneb:
             indexesofsorted.append(kuch.index(i))
             kuch[kuch.index(i)] = 'Fuck'
             notallowed.append(0)
         greedydone = []
         j = 0
         for i in sortneb:
             indexofi = indexesofsorted[j]
             #print("Index of i = ",indexofi) 4 5 4 3 4 5 2 5 -1 -1 10 1
             j += 1
             if i >= 0 and notallowed[indexofi] == 0:
                 currentchoice = neb[indexofi]
                 summ = 0
                 flag = 0
                 if indexofi == 0:
                     if notallowed[indexofi + 1] == 0:
                         summ += neb[indexofi + 1]
                     flag = 1
                 elif indexofi == n-1:
                     if notallowed[indexofi - 1] == 0:
                         summ += neb[indexofi - 1]
                     flag = 2
                 else:
                     if notallowed[indexofi - 1] == 0:
                         summ += neb[indexofi - 1]
                     if notallowed[indexofi + 1] == 0:
                         summ += neb[indexofi + 1]
                     flag = 3
                 if summ >= currentchoice:
                     if flag == 1:
                         greedydone.append(indexofi + 1)
            #             print(1)
                         notallowed[indexofi] = 1
                         notallowed[indexofi + 1] = 1
                         if indexofi +1 != n-1:
                             notallowed[indexofi + 2] = 1
                     elif flag == 2:
            #             print(2)
                         greedydone.append(indexofi - 1)
                         notallowed[indexofi] = 1
                         notallowed[indexofi - 1] = 1
                         if indexofi -1  != 0 :
                             notallowed[indexofi - 2] = 1
                     else:
                         greedydone.append(indexofi + 1)
            #             print(3)
                         greedydone.append(indexofi - 1)
                         notallowed[indexofi] = 1
                         notallowed[indexofi + 1] = 1
                         notallowed[indexofi - 1] = 1
                         if indexofi +1 != n-1:
                             notallowed[indexofi + 2] = 1
                         if indexofi -1  != 0 :
                             notallowed[indexofi - 2] = 1
                 else:
                     if flag == 1:
            #             print(4)
                         greedydone.append(indexofi)
                         notallowed[indexofi] = 1
                         notallowed[indexofi + 1] = 1
                     elif flag == 2:
                         greedydone.append(indexofi)
            #             print(5)
                         notallowed[indexofi] = 1
                         notallowed[indexofi - 1] = 1
                     else:
                         greedydone.append(indexofi)
            #             print(6)
                         notallowed[indexofi] = 1
                         notallowed[indexofi + 1] = 1
                         notallowed[indexofi - 1] = 1


         print(greedydone)



main()
