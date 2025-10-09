"""
15. Write a Python program to concatenate two tuples and create a new tuple. And then write a 
Python program to extract a slice of elements from the new tuple.
"""


tuple1 = tuple(map(int,input("Enter Tuple 1 : ").split()))
tuple2 = tuple(map(int,input("Enter Tuple 2 : ").split()))

concantenate = tuple1 + tuple2
print("Concantenate : ",concantenate)

slice_tuple = concantenate[2:5]
print("Slice : ",slice_tuple)