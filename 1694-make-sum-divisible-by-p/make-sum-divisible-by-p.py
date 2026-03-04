class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums) % p#
        if total == 0:
            return 0
        last = {0: -1}
        cur = 0
        ans = len(nums)
        for i, num in enumerate(nums):
            cur = (cur + num) % p
            target = (cur - total + p) % p
            if target in last:
                ans = min(ans, i - last[target])
            last[cur] = i
        return ans if ans < len(nums) else -1
