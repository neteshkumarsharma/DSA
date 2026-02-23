class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        res = []
        queueFreq = {}
        wordsFreq = {}

        for q in queries:
            minchr = min(q)
            minFreq = 1
            for i in range(len(q)):
                if q[i] == minchr:
                    minFreq += 1
            queueFreq[q] = minFreq
        
        for w in words:
            minchr = min(w)
            minFreq = 1
            for i in range(len(w)):
                if w[i] == minchr:
                    minFreq += 1
            wordsFreq[w] = minFreq
        
        for q in queries:
            count = 0
            for w in words: 
                if queueFreq[q] < wordsFreq[w]:
                    count += 1
            res.append(count)
        return res