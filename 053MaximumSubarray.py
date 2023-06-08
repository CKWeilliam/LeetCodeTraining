class Solution:
    def maxSubArray(self, nums) -> int:
        local_sum , global_max = 0, 0
        for i in range(1 , len(nums)):
            local_sum = max(local_sum + nums[i], nums[i])
            global_max = max(local_sum, global_max)
        
        return global_max


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))