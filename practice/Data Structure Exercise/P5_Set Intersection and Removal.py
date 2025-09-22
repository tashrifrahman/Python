first_set = {23,42,65,57,78,83,29}
second_set = {57,83,29,67,73,43,48}
print("First Set:",first_set)
print("Second Set:",second_set)

intersection = first_set.intersection(second_set)
print("Intersection:",intersection)

for i in intersection:
      first_set.remove(i)
print("Remove common element from First Set : ",first_set)