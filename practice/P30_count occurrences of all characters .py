str = input()
char_dict = dict()
for i in str:
      count = str.count(i)
      char_dict[i] = count
print('Result:',char_dict)