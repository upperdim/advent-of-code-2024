l1 = [1, 2, 3]
l2 = l1

l2.pop(1)       # also pops l1
print(l1)

l3 = l1.copy()  # deep copy
l3.pop(1)       # l1 is safe
print(l1)
