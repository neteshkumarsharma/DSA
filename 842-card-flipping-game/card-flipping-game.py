class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = set()#
        for f, b in zip(fronts, backs):
            if f == b:
                same.add(f)
        
        result = float('inf')
        for f in fronts:
            if f not in same:
                result = min(result, f)
        for b in backs:
            if b not in same:
                result = min(result, b)
        
        return result if result != float('inf') else 0
