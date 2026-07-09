class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        streak = 0
        
        for num in nums:
            if num == 0:
                streak += 1
                count += streak   
            else:
                streak = 0
        
        return count