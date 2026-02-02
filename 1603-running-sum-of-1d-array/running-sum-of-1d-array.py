class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:#
        res = [0] * len(nums)
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            res[i] = total
        return res