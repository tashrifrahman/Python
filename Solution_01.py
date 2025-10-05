"""
1. Write a Python program and take a temperature input and print: 
   ● Cold (temp < 15) 
   ● Warm (15 ≤ temp < 30) 
   ● Hot (temp ≥ 30)
"""


temp = float(input("Enter temperature :"))
if temp < 15:
      print("Cold")
elif 15 <= temp < 30:
      print("Warm")
else:
      print("Hot")