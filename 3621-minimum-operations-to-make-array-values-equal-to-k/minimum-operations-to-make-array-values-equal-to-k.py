class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if min(nums) < k:
            return -1
        distinct_greater = set(x for x in nums if x > k)
        
        return len(distinct_greater)