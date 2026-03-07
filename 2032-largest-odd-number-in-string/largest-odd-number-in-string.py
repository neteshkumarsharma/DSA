class Solution:
    def largestOddNumber(self, num: str) -> str:
        nums = []
        for i in range(len(num)):
            nums.append(int(num[i]))
        s = ''
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] % 2 != 0:
                j = 0
                while j <= i:
                    s = s + (str(nums[j]))
                    j += 1
                break
        return s