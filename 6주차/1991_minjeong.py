# 순회 참고 https://codingstarter.tistory.com/6

def preorder(node): # 전위 : 자신->왼->오
    if node == '.': return
    print(node, end = "") # 자신
    preorder(tree[node][0]) # 왼쪽 
    preorder(tree[node][1]) # 오른쪽

def inorder(node): # 중위 : 왼->자신->오
    if node == '.': return
    inorder(tree[node][0])
    print(node, end = "")
    inorder(tree[node][1])

def postorder(node): # 후위 : 왼->오->자신
    if node == '.': return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end = "")
    
n = int(input())
tree = []
for i in range(n): # 트리 만들기
    root, left, right = input().split()
    tree[root] = (left, right) # tree[자신]=(왼,오) 형태로 저장
    
preorder('A') # 전위
print()
inorder('A') # 중위
print()
postorder('A') # 후위