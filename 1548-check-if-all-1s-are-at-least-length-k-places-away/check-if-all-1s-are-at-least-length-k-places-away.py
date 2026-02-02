class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        i = 0
        while i < len(nums) and nums[i] == 0:
            i += 1
        
        j = i + 1
        while j < len(nums):
            if nums[j] == 0:
                j += 1
                continue
                
            if nums[j] == 1:
                print(i, j) 
                if j - i - 1 < k: 
                    return False
                i = j
            j += 1 
        return True
