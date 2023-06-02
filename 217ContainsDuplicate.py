def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums = sorted(nums)
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            return True
        else:
            i += 1

    return False

nums = [1, 2, 3, 5]
print(containsDuplicate(nums))