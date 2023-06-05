def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    length = len(nums)
    left, right, answer = [0]*length, [0]*length, [0]*length,
    # 初始化Array

    left[0] = 1
    for i in range(1, length):
        left[i] = nums[i-1] * left[i-1]

    right[length - 1] = 1
    for i in reversed(range(length-1)):
        right[i] = nums[i + 1] * right[i + 1]
    
    for i in range(length):
        answer[i] = left[i] * right[i]

    return answer

nums = [1,2,3,4]
productExceptSelf(nums)