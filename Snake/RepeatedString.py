# Enter your code here. Read input from STDIN. Print output to STDOUT
#aba
#10
#which makes input as aba*3+a --> a is substring of aba of length 1, hence total characters = 10
#o/p = no of a's = 7
seq = input()
no = int(input())
l = len(seq)
acount = seq.count('a')
acount *= (no//l)
acount += (seq.count('a',0,(no%l)))
print(acount)

