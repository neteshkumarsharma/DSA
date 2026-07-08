class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(sorted(s))
        
        sorted_freq = dict(sorted(freq.items(), key = lambda item: item[1], reverse =True))

        t = ''

        for key, val in sorted_freq.items():
            for i in range(val):
                t = t + key

        return t