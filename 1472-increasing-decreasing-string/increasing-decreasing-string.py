class Solution:
    def sortString(self, s: str) -> str:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        
        result = []
        remaining = len(s)
        
        while remaining > 0:
            for i in range(26):
                if count[i] > 0:
                    result.append(chr(i + ord('a')))
                    count[i] -= 1
                    remaining -= 1
            
            for i in range(25, -1, -1):
                if count[i] > 0:
                    result.append(chr(i + ord('a')))
                    count[i] -= 1
                    remaining -= 1
                    
        return "".join(result)