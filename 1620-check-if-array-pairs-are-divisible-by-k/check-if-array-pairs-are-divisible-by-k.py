class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        table = Counter()#
        for a in arr:
            table[a % k] += 1
        for r, count in table.items():
            if r == 0:
                if count % 2 != 0:
                    return False
            else:
                pair_r = k - r
                if table[pair_r] != count:
                    return False
        return True