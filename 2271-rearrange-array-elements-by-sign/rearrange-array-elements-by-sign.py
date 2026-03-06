class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        odds = []
        evens = []
        for num in nums:
            if num < 0:
                odds.append(num)
            else:
                evens.append(num)
        res = []
        i = 0
        k = 0
        while k < len(nums) / 2:
            res.append(evens[i])
            res.append(odds[i])
            i += 1
            k += 1
        return res