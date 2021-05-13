import sys
a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
a = int(a)
b = int(b)

first = b%10
second = b//10%10
third = b//100

print(a*first)
print(a*second)
print(a*third)

print((a*first)+(a*second)*10+(a*third)*100)