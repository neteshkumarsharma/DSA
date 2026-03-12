class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            total = sum((num + mid - 1) // mid for num in nums)
            if total <= threshold:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans