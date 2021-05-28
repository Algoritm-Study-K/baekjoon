#다시 해보기...

T = int(input())

def AC(cmd,n, deque):
    cmd.replace('RR', '')
    l, r, d = 0, 0, True
    for c in cmd:
        if c == 'R': d = not d
        elif c == 'D':
            if d: l += 1
            else: r += 1
    if l+r <= n:
        res = deque[l:n - r]
        if d: return '[' + ','.join(res) + ']\n'
        else: return '[' + ','.join(res[::-1]) + ']\n'
    else:
        return 'error\n'

for _ in range(T):
    cmd = input()
    n = int(input())
    deque = input().rstrip()[1:-1].split(',')
    if n == 0 : []
    print(AC(cmd, n, deque))
