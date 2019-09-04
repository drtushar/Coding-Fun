# Armstrong Number : Order considered 3

order = 3
number = raw_input("Enter Number to find Armstrong no : ")
temp = 0
for i in number:
    temp += pow(int(i),order)
if temp == int(number):
    print("{0} is Armstrong number".format(number))
else:
    print("{0} is not Armstrong numer".format(number))
#TuShAr12@21
