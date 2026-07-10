from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        freq_one = []
        
        for i in range(len(arr)):
            bin_number = format(arr[i], 'b')
            count = str(bin_number).count('1')
            freq_one.append((arr[i], count))
        
        freq_one.sort(key=lambda item: (item[1], item[0]))

        return [item[0] for item in freq_one]