"""
19. Given two tuples of integers, write a Python program to perform element-wise addition, 
subtraction, and multiplication and create new tuples for each operation. 
"""


tuple1 = tuple(map(int,input("Enter Tuple1 : ").split()))
tuple2 = tuple(map(int,input("Enter Tuple2 : ").split()))

if len(tuple1) != len(tuple2):
      print("Error")
else:
      addition       = tuple(tuple1[i] + tuple2[i] for i in range(len(tuple1)))
      subtraction    = tuple(tuple1[i] - tuple2[i] for i in range(len(tuple1)))
      multiplication = tuple(tuple1[i] * tuple2[i] for i in range(len(tuple1)))
      

      print("\nAddition : ",addition)
      print("\nSubtraction : ",subtraction)
      print("\nMultiplication : ",multiplication)
