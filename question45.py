# Input list
data = [1, 2, 2, 3]

# Create an empty dictionary to store frequency
frequency = {}

# Count frequency of each element
for item in data:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

# Display result
print("Frequency of elements:", frequency)