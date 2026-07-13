class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums) - 2):
            first, second, third = nums[i], nums[i+1], nums[i+2]
            if second % 2 == 0 and first + third == second // 2:
                count += 1
        return count