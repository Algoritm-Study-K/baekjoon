import sys
a, b = sys.stdin.readline().rstrip().split()
a = int(a)
b = int(b)
#print(round(a/b, 20)) #round(숫자, 소수점 자리수)
print(format(a/b, '.20f'))