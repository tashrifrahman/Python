"""
4. Write a Python program and take two loss values as input (model_1_loss, model_2_loss) and 
print which model performs better.
"""


model_1 = float(input("Model_1_Loss :"))
model_2 = float(input("Model_2_Loss :"))

if model_1 > model_2:
      print("model 1 performs better")
else:
      print("model 2 performs better.")