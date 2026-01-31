class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:#
        def cost(start):  
            total = 0
            n = len(nums)
            for i in range(start, n, 2):
                decrease = 0
                
                if i > 0:
                    decrease = max(decrease, nums[i] - nums[i-1] + 1)
                
                if i < n - 1:
                    decrease = max(decrease, nums[i] - nums[i+1] + 1)
                
                total += max(decrease, 0)
            return total
        
        return min(cost(0), cost(1))
