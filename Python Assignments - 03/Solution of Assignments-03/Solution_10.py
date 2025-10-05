"""
10. Write a Python program with the input: 
problem_type (classification/regression) and dataset_size. 
    ● If classification: 
        ○ If dataset_size ≤ 5000 → "Logistic Regression" 
        ○ Else → "Neural Network" 
    ● If regression: 
        ○ If dataset_size ≤ 10000 → "Linear Regression" 
        ○ Else → "XGBoost"
"""


problem_type = input("Problem Type (classification/regression) :").lower()
dataset_size = int(input("Dataset Size :"))

if problem_type == "classification":
      if dataset_size <= 5000:
            print("Logistic Regression")
      else:
            print("Neural Network")
elif problem_type == "regression":
      if dataset_size <= 10000:
            print("Linear Regression")
      else:
            print("XGBoost")