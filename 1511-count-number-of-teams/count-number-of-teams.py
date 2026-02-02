class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        for j in range(len(rating)):
            leftMin, leftMax = 0, 0
            rightMin, rightMax = 0, 0

            for i in range(j):
                if rating[i] < rating[j]:
                    leftMin += 1
                else:
                    leftMax += 1
                
            for k in range(j + 1, len(rating)):
                if rating[k] < rating[j]:
                    rightMin += 1
                else:
                    rightMax += 1
            
            res += leftMin * rightMax
            res += leftMax * rightMin
        return res