my_dict = {'name': 'Tashrif', 'age': 23, 'city': 'Chandpur', 'profession': 'Engineer'}
print(f"Dictionary:{my_dict}")

del my_dict['profession']
print(f"After Delete Dictionary:{my_dict}")

print("All key-value pairs:")
for key,value in my_dict.items():
      print(f"{key}: {value}")

def key_exists(dictionary,key_check):
      return key_check in dictionary
key1 = 'age'
print(f"{key1} exist : {key_exists(my_dict,key1)}")