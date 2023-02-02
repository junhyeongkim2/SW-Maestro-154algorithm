#1406 에디터
import sys

st1 = list(sys.stdin.readline().rstrip())
st2 = []

n = int(sys.stdin.readline())

for i in range(n):
    arr = list(sys.stdin.readline().split())
    if arr[0]=="P":
        st1.append(arr[1])
    elif arr[0] == "B":
        if len(st1) != 0 :
            st1.pop()
    elif arr[0] =="D":
        if len(st2) !=0:
            st1.append(st2.pop())
    elif arr[0] == "L":
        if len(st1) !=0:
            st2.append(st1.pop())
            
answer = st1+st2[::-1]
for i in answer:
    print(i,end="")

"""
print(''.join(stk1+list(reversed(stk2))))
이렇게도 가능

"""