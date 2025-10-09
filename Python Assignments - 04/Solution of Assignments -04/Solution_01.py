"""
1. Write a Python function called `factorial` that takes an integer as input and returns its factorial. 
Test the function with different values. 
"""


def factorial(n):
      if n<0:
            return "Invalid."
      if n==0:
            return 1
      result = 1
      for i in range(1, n+1):
            result *= i
      return result

n = int(input("Enter a number : "))
print("Factorial : ",factorial(n))