class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        j = n - 1
        while j > 0 and arr[j - 1] <= arr[j]:
            j -= 1
        if j == 0:
            return 0
        ans = j
        i = 0
        while i < n:
            if i > 0 and arr[i - 1] > arr[i]:
                break
            while j < n and arr[i] > arr[j]:
                j += 1
            ans = min(ans, j - i - 1)
            i += 1
        return ans
