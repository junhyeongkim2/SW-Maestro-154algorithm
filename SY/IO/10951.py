# 종료조건이 없음 -> EOF 문제
while True:
	try:
		a,b=map(int,input().split())
		print(a+b)
	except:
		break