"""
3. Write a Python function called `even_or_odd` that takes an integer as input and returns “Even” if 
the number is even and “Odd” if the number is odd. Test the function with different numbers.
"""


def even_or_odd(n):
      if n % 2 == 0:
            return "Even"
      else:
            return "Odd"
      
n = int(input("Enter number : "))
print("Even Or Odd :",even_or_odd(n))