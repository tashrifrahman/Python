"""
5. Write a Python function called `Greatest Common Divisor (GCD)` that takes two integers as input 
and returns their greatest common divisor. Test the function with different pairs of numbers.
"""


def gcd(a, b):
      result = 1
      for i in range (1, min(a, b)+1):
            if a % i == 0 and b % i == 0:
                  result = i
      return result


a, b = map(int, input("Enter two numbers : ").split())
print("GCD :",gcd(a, b))