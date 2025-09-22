n=int(input())
a=list(map(int,input().split()))
sorted_list = sorted(set(a))
print(sorted_list[-2])