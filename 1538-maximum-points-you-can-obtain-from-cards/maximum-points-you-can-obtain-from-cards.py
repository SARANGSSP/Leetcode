class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k == len(cardPoints):
            return sum(cardPoints)
        lsum = 0
        rsum = 0
        l = 0
        r = n-1
        maxsum = 0
        for i in range(k):
            lsum += cardPoints[i]
        maxsum = lsum
        
        for i in range(k-1,-1,-1):
            lsum = lsum - cardPoints[i]
            rsum += cardPoints[r]
            maxsum = max(lsum + rsum, maxsum)
            r -= 1
        return maxsum 