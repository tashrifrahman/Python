"""
17. Write a Python program and take Input: learning_rate = 0.1. 
    While learning_rate > 0.001, divide learning_rate by 2 and print each value.
"""


learning_rate = 0.1
while learning_rate > 0.001:
      learning_rate /= 2
      print("Update Learning Rate :",learning_rate)