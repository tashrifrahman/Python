"""
18. Write a Python program and take input: dataset_labels (number of labels). 
    Use a while loop to count even labels only. 
"""


dataset_labels = int(input("Enter dataset label : "))
count = 0
labels = 1

while labels <= dataset_labels:
      if labels % 2 == 0:
            count += 1
      labels +=1
print("Count Even Labels : ",count)