s = {1,8,2,3}
# print(len(s))
# s.remove(8)
# print(s)
# s.pop()
# print(s)
# s.pop()
# print(s)

# s.clear()
# print(s)

set1 ={1,2,3,4,5}
set2 = set1.union({5,3,2,1})
# print(set2)

set3 = set2.intersection({0})
print(set3)

# len(s): Returns 4, the length of the set
# s.remove(8): Updates the set s and removes 8 from s.
# s.pop(): Removes an arbitrary element from the set and return the element removed.
# s.clear(): empties the set s.
# s.union({8,11}): Returns a new set with all items from both sets.
# s.intersection({8,11}): Returns a set which contains only item in both sets {8}.