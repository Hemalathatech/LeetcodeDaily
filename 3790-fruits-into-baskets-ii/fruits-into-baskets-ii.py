class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n = len(fruits)
        used = [False] * n  
        unplaced = 0

        for f in fruits:
            placed = False
            for j in range(n):
                if not used[j] and baskets[j] >= f:
                    used[j] = True
                    placed = True
                    break
            if not placed:
                unplaced += 1

        return unplaced