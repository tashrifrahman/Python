"""
20. Write a Python program and take input: marks (0-100). 
     ● If marks ≥ 80 → "AI Expert" 
     ● Else if marks ≥ 60 → "AI Learner" 
     ● Else → "Needs Improvement"
"""


marks = float(input("Enter Marks (0-100) : "))

if marks >= 80:
      print("AI Expert")
elif marks >= 60:
      print("AI Learner")
else:
      print("Needs Improvement")