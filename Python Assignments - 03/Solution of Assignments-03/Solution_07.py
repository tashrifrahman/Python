"""
7. Write a Python program with the following inputs: accuracy and latency (ms). 
     ● If Accuracy ≥ 85: 
          ○ If Latency ≤ 100ms → "Ready for Production" 
          ○ Else → "Needs Optimization" 
     ● Else → "Not Suitable for Deployment"
"""


accuracy = float(input("Enter Accuracy :"))
latency = float(input("Enter Latency (ms) :"))

if accuracy >= 85:
      if latency <= 100:
            print("Ready for Production")
      else:
            print("Needs Optimization")
else:
      print("Not Suitable for Deployment")