def io(li):
	for i in li:
		if i==' ':
			st[3]+=1
		elif i.isdigit():
			st[2]+=1
		elif i.isupper():
			st[1]+=1
		else:
			st[0]+=1

while True:
	try:
		st=[0,0,0,0]
		li=list(input())
		io(li)

		for i in st:
			print(i,end=' ')
		print()
	except EOFError:
		break