"""
7. Write a Python function called `math_operations` that takes three numbers and a string 
representing an operation (‘add’, ‘subtract’, ‘multiply’, or ‘divide’). The function should return the 
result of the specified operation on the three numbers. Implement the math operations as nested 
functions.
"""


def math_operations(a, b, c, operation):
      def add(a,b,c):
            return a + b + c
      def subtract(a,b,c):
            return a - b - c
      def multiply(a,b,c):
            return a * b * c
      def divide(a,b,c):
            return a / b / c
      

      if operation == "add":
            return add(a,b,c)
      elif operation == "subtract":
            return subtract(a,b,c)
      elif operation == "multiply":
            return multiply(a,b,c)
      elif operation == "divide":
            return divide(a,b,c)
      
a, b, c = map(float,input("Enter three numbers : ").split())
operation = input("Enter operation(add, subtract, multiply, or divide) : ").lower()

result = math_operations(a,b,c,operation)
print("Result : ",result)
