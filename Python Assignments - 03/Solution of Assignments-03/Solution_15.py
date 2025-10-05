"""
15. Write a Python program and take input: a number. 
    Use a while loop to keep dividing the number by 2 until the value ≤ 1. Print each step.
"""


number = float(input("Enter a Number : "))
i=0
while number > 1:
      number /= 2
      i += 1
      print (f"Step {i} : {number}")