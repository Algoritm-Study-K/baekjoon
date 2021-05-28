#다시 해보기...
from itertools import combinations
            
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

num_list = [i for i in range(n)]
res = float('inf')            

def solve():
    global res
    
    for cand in combinations(num_list, n // 2):
        start_member = list(cand)
        link_member = list(set(num_list) - set(cand))
        
        start_combi = list(combinations(start_member, 2))
        link_combi = list(combinations(link_member, 2))
        
        team_start = 0
        for x, y in start_combi:
            team_start += (board[x][y] + board[y][x])
            
        team_link = 0
        for x, y in link_combi:
            team_link += (board[x][y] + board[y][x])
        
        if(res > abs(team_start - team_link)):
            res = abs(team_start - team_link)

solve()
print(res)