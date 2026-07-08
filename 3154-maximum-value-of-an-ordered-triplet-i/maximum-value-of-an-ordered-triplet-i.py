class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_right = [0] * n
        max_right[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            max_right[i] = max(nums[i], max_right[i+1])
        
        ans = 0
        max_left = nums[0]
        
        for j in range(1, n-1):
            value = (max_left - nums[j]) * max_right[j+1]
            ans = max(ans, value)
            max_left = max(max_left, nums[j])
        
        return ans
    