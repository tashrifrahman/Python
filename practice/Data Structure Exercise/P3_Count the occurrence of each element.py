sample_list = [11,45,8,11,23,45,23,89]
print("List:",sample_list)

count = dict()
for i in sample_list:
      if i in count:
            count[i] += 1
      else:
            count[i] = 1

print("Count the each item :",count)