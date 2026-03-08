class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxPro = nums[0]
        minPro = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            tempMaxPro = maxPro
            tempMinPro = minPro

            maxPro = max(num, tempMaxPro * num, tempMinPro * num)
            minPro = min(num, tempMaxPro * num, tempMinPro * num)

            result = max(maxPro, result)
        return result