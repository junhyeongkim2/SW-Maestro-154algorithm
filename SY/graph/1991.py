class Node:
	def __init__(self, data, left, right):
		self.data=data
		self.left=left
		self.right=right

n=int(input())
tree={}

for i in range(n):
	data, left, right=input().split()
	if left=='.':
		left=None
	if right=='.':
		right=None
	tree[data]=Node(data,left,right)

#전위 순회: 루트 -> 왼쪽 자식 -> 오른쪽 자식
def pre_order(node):
	print(node.data,end='')
	if node.left!=None:
		pre_order(tree[node.left])
	if node.right!=None:
		pre_order(tree[node.right])

#중위 순회: 왼쪽 자식 -> 루트 -> 오른쪽 자식
def in_order(node):
	if node.left!=None:
		in_order(tree[node.left])
	print(node.data,end='')
	if node.right!=None:
		in_order(tree[node.right])

#후위 순회: 왼쪽 자식 -> 오른쪽 자식 -> 루트
def post_order(node):
	if node.left!=None:
		post_order(tree[node.left])
	if node.right!=None:
		post_order(tree[node.right])
	print(node.data,end='')

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
