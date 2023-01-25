import sys
input = sys.stdin.readline
total = int(input())
tree = {}

for _ in range(total):
    root , left, right = map(str, input().split())
    tree[root] = left, right

def preorder(root):
    if root != '.':
        print(root, end = "")
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end = "")
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end = "")
    

preorder('A')
print()
inorder('A')
print()
postorder('A')