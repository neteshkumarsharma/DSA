class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True) 
        
        fleets = 0
        prev_time = 0.0  
        
        for pos, spd in pairs:
            time = (target - pos) / spd  
            if time > prev_time:
                fleets += 1
                prev_time = time  
        
        return fleets
