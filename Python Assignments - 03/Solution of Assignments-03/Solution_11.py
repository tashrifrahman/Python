"""
11. Write a Python program and take an initial loss value as input. 
    While loss > 0.1: subtract 0.05 each iteration and print loss. 
"""


loss = float(input("Enter initial loss value :"))
while loss > 0.1:
      loss -= 0.05
      print(f"Loss : {loss:.2f}")