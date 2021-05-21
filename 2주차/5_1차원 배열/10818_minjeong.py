num=int(input())
#num_list=[None]*num
num_list = list(map(int,input().split()))
print(min(num_list), max(num_list))