class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one = -k - 1 
        for i, num in enumerate(nums):
            if num == 1:
                if i - last_one - 1 < k:
                    return False
                last_one = i
        return True

