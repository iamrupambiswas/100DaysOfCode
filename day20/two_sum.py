def twoSum(nums, target):
    start = 0
    end = len(nums) - 1
    while start < end:
        result = nums[start] + nums[end]
        if result == target:
            return [start,end]
        elif result > target:
            end = end-1
        else:
            start = start + 1
            
print(twoSum([2,7,11,15],9))