maxor = 0
nums = [2,4]
while(len(nums)>1):
	for i in range(len(nums)):
		cur = nums[0]^nums[i]
		if cur > maxor:
			maxor = cur
	nums = nums[1:]
print(maxor)
