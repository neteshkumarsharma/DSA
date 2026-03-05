class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = []

        if k == 0:
            return [0] * n

        for i in range(n):
            totalVal = 0
            if k > 0:
                for j in range(1, k + 1):
                    totalVal += code[(i + j) % n]
            else:
                for j in range(1, -k + 1):
                    totalVal += code[(i - j) % n]
            res.append(totalVal)

        return res
