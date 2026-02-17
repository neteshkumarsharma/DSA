class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = Counter(arr)
        freq = sorted(counts.values())
        removedElements = 0
        for f in freq:
            if k >= f:
                k -= f
                removedElements += 1 
            else:
                break
        return len(freq) - removedElements