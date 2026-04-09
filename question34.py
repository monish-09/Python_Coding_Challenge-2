nums = [1, 1, 2, 3, 3]

unique = []

for n in nums:
    if n not in unique:
        unique.append(n)

print("Unique count:", len(unique))