num1,num2 = 0,1 #first two numbers
print("Fibonacci series:")

for i in range(15):
      print(num1, end=" ")
      res = num1 + num2

      num1 = num2
      num2 = res