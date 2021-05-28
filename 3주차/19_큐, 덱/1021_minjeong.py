<<<<<<< HEAD
#다시 해보기...
n, m = map(int, input().split())
seq = list(map(int ,input().split()))

deque = [i for i in range(1, n + 1)]
cnt = 0

for i in range(m):
    q_len = len(deque)
    q_idx = deque.index(seq[i])
    if q_idx < q_len - q_idx:
        while True:
            if deque[0] == seq[i]:
                del deque[0]
                break
            else:
                deque.append(deque[0])
                del deque[0]
                cnt += 1
    else:
        while True:
            if deque[0] == seq[i]:
                del deque[0]
                break
            else:
                deque.insert(0, deque[-1])
                del deque[-1]
                cnt += 1
print(cnt)
=======
#다시 해보기...
n, m = map(int, input().split())
seq = list(map(int ,input().split()))

deque = [i for i in range(1, n + 1)]
cnt = 0

for i in range(m):
    q_len = len(deque)
    q_idx = deque.index(seq[i])
    if q_idx < q_len - q_idx:
        while True:
            if deque[0] == seq[i]:
                del deque[0]
                break
            else:
                deque.append(deque[0])
                del deque[0]
                cnt += 1
    else:
        while True:
            if deque[0] == seq[i]:
                del deque[0]
                break
            else:
                deque.insert(0, deque[-1])
                del deque[-1]
                cnt += 1
print(cnt)
>>>>>>> 9bfce3ba1e6ddd95a242c42c05eb89b114e96440
