class Solution:
    def countLargestGroup(self, n: int) -> int:
        sum_counts = {}
    
        for i in range(1, n + 1):
            digit_sum = 0
            temp = i
            while temp > 0:
                digit_sum += temp % 10
                temp //= 10
                
            sum_counts[digit_sum] = sum_counts.get(digit_sum, 0) + 1
            
        max_size = max(sum_counts.values())
        
        return sum(1 for size in sum_counts.values() if size == max_size)