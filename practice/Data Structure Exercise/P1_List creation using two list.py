list1=[3,6,9,12,15,18,21]
list2 = [4,8,12,16,20,24,28]

result = list()

odd_element = list1[1::2]
print("Odd-index Element from List1:",odd_element)

even_element = list2[0::2]
print("Even-index Element:",even_element)

result.extend(odd_element)
result.extend(even_element)
print("Final Thirs List:",result)
