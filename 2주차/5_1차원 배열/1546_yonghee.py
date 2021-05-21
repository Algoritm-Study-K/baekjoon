N = int(input())
score = list(map(int, input().split()))
M = max(score)
sum = 0

for i in range(N):
	sum += score[i] / M * 100
print(sum / N)