n=int(input())
print(n, end=" ")
while (n != 1):
      if n % 2 == 0:
             print(n // 2, end =" ")
             n = n // 2
      else:
             print(3 * n + 1, end=" ")
             n = 3 * n + 1
