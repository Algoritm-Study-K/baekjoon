from sys import stdin

N = int(input())

members = []

for i in range(N):
	[age, name] = stdin.readline().split()
	members.append([age, name])

members.sort(key = lambda x: int(x[0]))
for i in range(N):
	print(members[i][0], members[i][1])