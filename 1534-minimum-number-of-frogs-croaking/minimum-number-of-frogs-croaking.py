class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c = r = o = a = 0
        
        max_frogs = 0
        current_frogs = 0
        
        for ch in croakOfFrogs:
            if ch == 'c':
                c += 1
                current_frogs += 1
                max_frogs = max(max_frogs, current_frogs)
            elif ch == 'r':
                if c == 0: return -1
                c -= 1
                r += 1
            elif ch == 'o':
                if r == 0: return -1
                r -= 1
                o += 1
            elif ch == 'a':
                if o == 0: return -1
                o -= 1
                a += 1
            elif ch == 'k':
                if a == 0: return -1
                a -= 1
                current_frogs -= 1 
            else:
                return -1  
                
        if current_frogs > 0:
            return -1
            
        return max_frogs