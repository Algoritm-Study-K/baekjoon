# 시간초과... 코드는 맞는 것 같은데 시간 초과나는 코드 찾아야함
# dfs 사용

def dfs(tree, s, parent):
    for i in tree[s]: #1부터 인접한 노드 탐색
        if parent[i] == 0: # 방문 x 노드는 부모 노드로 저장
            parent[i] = s
            dfs(tree, i, parent)

n = int(input())
tree = [[] for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)] # 부모 노드 저장

for _ in range(n - 1): # 트리 제작
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(tree, 1, parent) # 1부터 시작

for i in range(2, n + 1): # 1은 빼고 세기
    print(parent[i])