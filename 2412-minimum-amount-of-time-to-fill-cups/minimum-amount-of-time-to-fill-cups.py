class Solution(object):
    def fillCups(self, amount):
        """
        :type amount: List[int]
        :rtype: int
        """
        total = sum(amount)
        largest = max(amount)
        return max(largest, (total + 1) // 2)