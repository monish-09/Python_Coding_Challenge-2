# Input list
numbers = [1, 2, 4, 5]

# Calculate expected sum of numbers from min to max
expected_sum = sum(range(min(numbers), max(numbers) + 1))

# Calculate actual sum
actual_sum = sum(numbers)

# Find the missing number
missing_number = expected_sum - actual_sum

print("Missing number:", missing_number)