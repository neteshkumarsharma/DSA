class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def findDays(weights, cap):
            days, load = 1, 0
            for w in weights:
                if load + w > cap:
                    days += 1
                    load = w
                else:
                    load += w
            return days
        
        low, high = max(weights), sum(weights)

        while low <= high:
            mid = low + (high - low) // 2
            numberOfDays = findDays(weights, mid)
            if numberOfDays <= days:
                high = mid - 1
            else:
                low = mid + 1
        return low