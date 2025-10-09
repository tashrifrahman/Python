"""
13. Write a Python program to transpose a given matrix represented as a nested list.
"""


def transpose_matrix(matrix):
      rows = len(matrix)
      cols = len(matrix[0])
      transpose = [[matrix[i][j] for i in range(rows)] for j in range(cols)]
      return transpose


rows = int(input("Enter number of rows : "))
cols = int(input("Enter number of coloums : "))

matrix = []
for i in range(rows):
      row = list(map(int,input(f"Row {i+1}: ").split()))
      matrix.append(row)

result = transpose_matrix(matrix)

print("Orginal Matrix : ")
for row in matrix:
      print(row)

print("\nTransposed Matrix : ")
for row in result:
      print(row)