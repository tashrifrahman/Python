word = input('Enter word:')
print("orginal string:",word)
size = len(word)
for i in range(0,size,2):
      print("index[", i, "]",word[i])