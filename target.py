def twoSum(nums, target):
	seen = {}
	for i in range(0,len(nums)):
		if (target-nums[i]) in seen:
			return [seen[target - nums[i]],i]
		else:
			seen[nums[i]] = i

nums = [3,2,8,4]
target = 6

print(twoSum(nums,target))
