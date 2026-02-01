class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window = sum(cardPoints[-k:])
        max_score = window
        n = len(cardPoints)
        for i in range(k):
            window += cardPoints[i] - cardPoints[n - k + i] 
            max_score = max(max_score, window)
            
        return max_score
