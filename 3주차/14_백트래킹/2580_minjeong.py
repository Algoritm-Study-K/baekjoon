#코드 보고함
import sys

board = []
for i in range(9):  
  board.append(list(map(int, input().split())))

zero = []
for i in range(9):
  for v in range(9):
    if board[i][v] == 0 :
      zero.append([i, v])

row_sum = [0 for _ in range(9)]
column_sum = [0 for _ in range(9)]
rec_sum = [0 for _ in range(9)]

def check(index, r, c):
  number_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
  
  for i in range(9):
    if board[r][i] in number_set:
      number_set.remove(board[r][i])
    if board[i][c] in number_set:
      number_set.remove(board[i][c])

  for i in range(r - r%3 , r - r%3 +3):
    for v in range(c- c%3 , c- c%3 +3):
      if board[i][v] in number_set:
        number_set.remove(board[i][v])
  
  return number_set


def dfs(index, number):
  global reset

  if index != 0:
    prev_r, prev_c = zero[index - 1]
    board[prev_r][prev_c] = number
  
  if index==len(zero):
    for n in range(9):
      print(" ".join(map(str, board[n])))
    sys.exit()
  
  r, c = zero[index]

  for number in check(index, r, c):
    board[r][c] = number
    dfs(index+1, number)
    board[r][c] = 0

dfs(0, 0)