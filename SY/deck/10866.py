from collections import deque
import sys

n=int(sys.stdin.readline())
li=[sys.stdin.readline().strip('\'\n') for _ in range(n)]
deque=deque()

for i in li:
	if 'push_front' in i:
		deque.appendleft(i[11:])
	elif 'push_back' in i:
		deque.append(i[10:])
	elif 'pop_front'==i:
		if deque:
			print(deque.popleft())
		else:
			print(-1)
	elif 'pop_back'==i:
		if deque:
			print(deque.pop())
		else:
			print(-1)
	elif 'size'==i:
		print(len(deque))
	elif 'empty'==i:
		if not deque:
			print(1)
		else:
			print(0)
	elif 'front'==i:
		if deque:
			print(deque[0])
		else:
			print(-1)
	elif 'back'==i:
		if deque:
			print(deque[-1])
		else:
			print(-1)