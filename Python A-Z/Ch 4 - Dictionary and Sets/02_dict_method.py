oxford={
      "gift":"Something willingly given to someone to appreciate",
      "this":"A keyword in c++",
      "Youtube":"A video sharing platform",
      "mylist":[1,3,45]
}
# print(oxford.items())

oxford.update({"tashrif":"Good boy","mylist":[56,8]})

for a,b in oxford.items(): # a = key, b = value
      print(a,":",b)

for key in oxford.keys():
      print(key)

oxford.update({"tashrif":"Good boy","mylist":[56,8]})

print(oxford.get('notpresent'))