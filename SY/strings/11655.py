st=list(input())
for i in range(len(st)):
	if st[i].isalpha():
		if st[i].isupper():
			st[i]=chr((ord(st[i])-65+13)%26+65)
		elif st[i].islower():
			st[i]=chr((ord(st[i])-97+13)%26+97)

for i in st:
	print(i,end='')
