class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        capTime = float("-inf")
        fleets = 0
        for carPos, carSpeed in pairs:
            duration = (target -  carPos)/carSpeed
            if capTime < duration:
                capTime = duration
                fleets += 1
        
        return fleets


# 1/1 -> 10 at time 3 = (10-1)/3
# 4/2 -> 10 at time 3 = (10-4)/2




# 7/0.5 -> 10-7)0.5 = 6
# 4/2 -> 10-4)/2 = 3 -> 6
# 1/2 -> 10-1)/2 = 4.5 -> 6
# 0/1 -> 10-0)/1 = 10
