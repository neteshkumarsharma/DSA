class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        oddPreSum = [0] * (n + 1)
        evenPreSum = [0] * (n + 1)

        for i, num in enumerate(nums):
            if i % 2:
                oddPreSum[i + 1] = oddPreSum[i] + num
                evenPreSum[i + 1] = evenPreSum[i]
            else:
                evenPreSum[i + 1] = evenPreSum[i] + num
                oddPreSum[i + 1] = oddPreSum[i]
        print(oddPreSum, evenPreSum)
        ans = 0
        for i in range(1, n + 1):
            oddSum1 = oddPreSum[i - 1]
            evenSum1 = evenPreSum[i - 1]

            oddSum2 = oddPreSum[-1] - oddPreSum[i]
            evenSum2 = evenPreSum[-1] - evenPreSum[i]
            if oddSum1 + evenSum2 == evenSum1 + oddSum2:
                ans += 1

        return ans