class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        row_count = {}#
        
        for row, seat in reservedSeats:
            if 1 <= seat <= 10:  
                row_count.setdefault(row, [0]*11)[seat] = 1
        
        result = n * 2  
        
        for row in row_count.values():
           
            left_free = all(row[i] == 0 for i in [2,3,4,5])     
            right_free = all(row[i] == 0 for i in [6,7,8,9])      
            middle_free = all(row[i] == 0 for i in [4,5,6,7])   

            families = 0

            if left_free and right_free:
                families = 2
            elif left_free or right_free or middle_free:
                families = 1
            
            result -= (2 - families)  
        
        return result