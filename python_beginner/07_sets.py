# 1. Sets remove duplicate values:
s = {2, 3, 4, 3, 2, 6}
print("\n1. Sets remove duplicate values:", s)

# 2. Sets can store different types of values:
info = {"Carla", 29, False, 5.9, 29}
print("\n2. A single set can store different types of values: ", info)
print(type(info))

# 3. Creating empty dictionaries and sets:
print("\n3. Creating empty dictionaries and sets:")
harry = {}
print(type(harry))

potter = set()
print(type(potter))

# 4. Iterating through a set:
print("\n4. Iterating through a set:")
for value in info:
    print(value)

# 5. Set operations:
print("\n5. Set operations:")

s1 = {1, 2, 5, 6}
s2 = {2, 4, 5, 7}
print("   a. s1 Union s2: ", s1.union(s2))  
s1.update(s2)                                             # Updates s1 to union
print("   b. Updates s1 to union: s1=", s1)

s1 = {1, 2, 5, 6}
s_int = s1.intersection(s2) 
print("   c. s1 intersection s2: ", s_int)
s1.intersection_update(s2)                                # Updates s1 to intersection
print("   d. Updates s1 to intersection: s1=", s1)

s1 = {1, 2, 5, 6}
s_sd = s1.symmetric_difference(s2)                         
print("   e. Symmetric difference (s1-s2): ", s_sd)
s1.symmetric_difference_update(s2)                        # Updates s1 to symmetric difference
print("   f. Updates s1 to symmetric difference: s1=", s1)

s1 = {1, 2, 5, 6}
print("   g. s1 and s2 have no elements in common: ", s1.isdisjoint(s2))  # True if s1 and s2 have no elements in common
print("   h. s1 contains all elements of s2: ", s1.issuperset(s2))        # True if s1 contains all elements of s2
print("   i. s1 is contained in s2: ", s1.issubset(s2))                   # True if s1 is contained in s2
 
s1.add(7)
s1.add(4)
print("   Now s1=", s1)

print("   j. s1 contains all elements of s2: ", s1.issuperset(s2)) 
print("   k. s1 is contained in s2: ", s2.issubset(s1))  

# 6. Set methods:
print("\n6. Set methods:")

s1 = {1, 2, 5, 6}
# s1.remove(9)       # This will raise an error if 9 is not present
print(s1)

s1.discard(9)        # This will not raise an error if 9 is not present
print(s1)

print(s1.pop())      # Removes and returns an arbitrary element
print(s1)
print(s1.pop())
print(s1)
print(s1.pop())
print(s1)
print(s1.pop())
print(s1)

s1 = {1, 2, 5, 6}
# del s1             # Deletes the set entirely
print(s1)            # This will raise an error since s1 is deleted

s1.clear()           # Removes all elements from the set
print(s1)            # Should print an empty set

s1 = {1, 2, 5, 6}
print(1 in s1)

