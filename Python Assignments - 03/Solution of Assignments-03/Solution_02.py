"""  
2. Write a Python program and take accuracy input (0–100%). 
     ● If accuracy ≥ 90 → Excellent Model 
     ● If 70–89 → Good Model 
     ● If 50–69 → Average Model 
     ● Else → Poor Model 
"""


accuracy = int(input("Enter Accuracy :"))
if accuracy >= 90:
      print("Excellent Model")
elif 70 <= accuracy <= 89:
      print("Good Model")
elif 50 <= accuracy <= 69:
      print("Average Model")
else:
      print("Poor Model")
