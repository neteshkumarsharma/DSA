class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        result = high

        while low <= high:
            k = low + (high - low) // 2
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / k)
            if total_hours <= h:
                result = k
                high = k - 1
            else:
                low = k + 1
        return result