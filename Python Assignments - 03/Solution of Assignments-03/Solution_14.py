"""
14. Write a Python program and take input: total_epochs. 
    For each epoch, print "Training epoch X" until all epochs are completed.
"""


total_epochs = int(input("Enter total epochs : "))
count = 1
while count <= total_epochs:
      print("Training epoch ",count)
      count += 1