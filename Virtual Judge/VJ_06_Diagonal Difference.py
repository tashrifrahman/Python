def diagonal_difference(arr):
      n=len(arr)
      left_sum = 0
      right_sum = 0
      for i in range(n):
            left_sum += arr[i][i]
            right_sum += arr[i][n-1-i]
      return abs(left_sum-right_sum)

n=int(input())
arr = []
for i in range(n):
      row = list(map(int,input().split()))
      arr.append(row)
result = diagonal_difference(arr)
print(result)