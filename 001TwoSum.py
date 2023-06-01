
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    seen_dict = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen_dict:
            return [seen_dict[diff], i]
        else:
            seen_dict[nums[i]] = i

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))