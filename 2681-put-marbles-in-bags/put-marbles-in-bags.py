class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :rtype: int
        """
        n = len(weights)
        
        # Special case: only one bag → no cuts → difference is 0
        if k == 1:
            return 0
        if k == n:
            return 0  # each marble in its own bag → fixed score
        
        # Compute boundary costs
        boundaries = [weights[i] + weights[i+1] for i in range(n-1)]
        boundaries.sort()
        
        # Max score = sum of largest (k-1) boundaries
        max_score = sum(boundaries[-(k-1):])
        
        # Min score = sum of smallest (k-1) boundaries
        min_score = sum(boundaries[:k-1])
        
        return max_score - min_score