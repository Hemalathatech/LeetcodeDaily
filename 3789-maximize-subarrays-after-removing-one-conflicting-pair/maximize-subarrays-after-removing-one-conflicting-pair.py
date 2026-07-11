class Solution(object):
    def maxSubarrays(self, n, conflictingPairs):
        """
        :type n: int
        :type conflictingPairs: List[List[int]]
        :rtype: int
        """
        bMin1 = [n + 1] * (n + 2)
        bMin2 = [n + 1] * (n + 2)
        for a, b in conflictingPairs:
            if a > b: a, b = b, a
            if b < bMin1[a]:
                bMin2[a] = bMin1[a]
                bMin1[a] = b
            elif b < bMin2[a]:
                bMin2[a] = b
        
        res = 0
        delCount = [0] * (n + 2)
        firstBlock = n + 1
        secondBlock = n + 1
        idxBlock = -1
        
        # Sweep from right to left
        for i in range(n, 0, -1):
            if bMin1[i] < firstBlock:
                secondBlock = min(secondBlock, firstBlock)
                firstBlock = bMin1[i]
                idxBlock = i
            else:
                secondBlock = min(secondBlock, bMin1[i])
            
            # Count valid subarrays starting at i
            res += min(firstBlock, n + 1) - i
            
            # Candidate gain if we drop conflict at idxBlock
            if idxBlock != -1:
                gain = min(secondBlock, bMin2[idxBlock], n + 1) - min(firstBlock, n + 1)
                delCount[idxBlock] += gain
        
        return res + max(delCount)