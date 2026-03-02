class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            arr = nums[l[i]:r[i] + 1]
            arr.sort()
            diff = arr[1] - arr[0]
            app = True
            for i in range(1, len(arr)):
                if arr[i] - arr[i -1] != diff:
                    app = False
                    break
            res.append(app)
        return res