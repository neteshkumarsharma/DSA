class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            row = matrix[i] 
            
            start, end = 0, len(row) - 1
            while start <= end:
                mid_idx = (start + end) // 2  
                mid_val = row[mid_idx]        
                
                if mid_val == target:        
                    return True               
                elif target > mid_val:         
                    start = mid_idx + 1
                else:
                    end = mid_idx - 1  
        return False 
