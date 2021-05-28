result = []
def dfs(depth, n, m):
    if depth == m:
        print(' '.join(map(str, result))) #띄어쓰기도 합쳐서 저장
        return

    for i in range(1, n+1):
        result.append(i)
        dfs(depth+1, n, m)
        result.pop()

n, m = map(int, input().split())
dfs(0, n, m)