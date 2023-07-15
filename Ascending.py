def sort_list(nums):
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      if nums[i] > nums[j]:
        nums[i], nums[j] = nums[j], nums[i]

nums = [10, 5, 2, 3, 1]
sort_list(nums)
print("The sorted list is", nums)
