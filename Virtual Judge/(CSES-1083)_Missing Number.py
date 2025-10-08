n = int(input())
numbers = list(map(int, input().split()))

missing_number = sum(range(1, n+1)) - sum(numbers)
print(missing_number)