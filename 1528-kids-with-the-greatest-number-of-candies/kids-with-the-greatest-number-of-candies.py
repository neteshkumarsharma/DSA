class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandie = max(candies)
        candies = [candie + extraCandies for candie in candies]
        res = []
        for candie in candies:
            if candie >= maxCandie:
                res.append(True)
            else:
                res.append(False)
        return res