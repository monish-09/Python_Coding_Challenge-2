list1 = [1, 2, 3]
list2 = [2, 3, 4]

common = []

for n in list1:
    if n in list2 and n not in common:
        common.append(n)

print(common)