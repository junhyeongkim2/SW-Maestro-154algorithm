# 1991번 트리 순회
import sys
read = sys.stdin.readline

def preOrder(node):
    print(node, end='') # 현재 노드
    if graph[node][0] != '.': # 왼쪽이 비어있지 않은 경우
        preOrder(graph[node][0]) # 현재 노드의 왼쪽 값
    if graph[node][1] != '.': # 오른쪽이 비어있지 않은 경우
        preOrder(graph[node][1])

def inOrder(node):
    if graph[node][0] != '.': # 왼쪽이 비어있지 않은 경우
        inOrder(graph[node][0]) # 현재 노드의 왼쪽 값
    print(node, end='') # 현재 노드
    if graph[node][1] != '.': # 오른쪽이 비어있지 않은 경우
        inOrder(graph[node][1])

def postOrder(node):
    if graph[node][0] != '.': # 왼쪽이 비어있지 않은 경우
        postOrder(graph[node][0]) # 현재 노드의 왼쪽 값
    if graph[node][1] != '.': # 오른쪽이 비어있지 않은 경우
        postOrder(graph[node][1])
    print(node, end='') # 현재 노드

N = int(read().strip())
graph = dict()
for _ in range(N):
    g = read().split()
    graph[g[0]] = g[1:]

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')