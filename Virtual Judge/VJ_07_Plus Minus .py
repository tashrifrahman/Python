n=int(input())
arr = list(map(int, input().split()))

pos = sum(1 for i in arr if i > 0)
neg = sum(1 for i in arr if i < 0)
zero = sum(1 for i in arr if i == 0)

print(f"{pos/n:.6f}")
print(f"{neg/n:.6f}")
print(f"{zero/n:.6f}")