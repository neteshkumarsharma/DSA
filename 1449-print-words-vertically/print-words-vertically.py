class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()  
        max_len = max(len(word) for word in words)
        
        result = []
        for col in range(max_len):
            row = []
            for word in words:
                if col < len(word):
                    row.append(word[col]) 
                else:
                    row.append(' ')        
            
            while row and row[-1] == ' ':  
                row.pop()
            
            result.append(''.join(row)) 
        
        return result
