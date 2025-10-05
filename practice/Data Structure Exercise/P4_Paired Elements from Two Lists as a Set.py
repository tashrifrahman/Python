list1 = [2,3,4,5,6,7,8]
print("First List :",list1)
list2 = [4,9,16,25,36,49,64]
print("Second List :",list2)

result = zip(list1, list2)
result_set = set(result)
print(result_set)