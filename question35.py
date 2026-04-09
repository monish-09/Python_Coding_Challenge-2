nums = [5, 2, 9, 1]

for i in range(len(nums)):
    for j in range(0, len(nums)-i-1):
        if nums[j] > nums[j+1]:
            # swap
            nums[j], nums[j+1] = nums[j+1], nums[j]

print("Sorted list:", nums)