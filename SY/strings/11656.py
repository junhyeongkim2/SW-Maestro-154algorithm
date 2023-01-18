st=input()
li=[]

for i in range(len(st)):
	suf=st[i:]
	li.append(suf)
li.sort()

for i in li:
	print(i)