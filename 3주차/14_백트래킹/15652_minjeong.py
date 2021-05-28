result = []
def dfs(depth, index, n, m):
    if depth == m:
        print(' '.join(map(str, result)))
        return
        
    for i in range(index, n):
        result.append(i+1)
        dfs(depth+1, i, n, m)
        result.pop()

n, m = map(int, input().split())
dfs(0, 0, n, m)