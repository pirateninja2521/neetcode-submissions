class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eatingHours(piles, speed):
            return sum([math.ceil(pile / speed) for pile in piles])
        
        maxSpeed = max(piles)
        minSpeed = 1

        while minSpeed < maxSpeed:
            mid = (maxSpeed + minSpeed) // 2

            if eatingHours(piles, mid) <= h:
                maxSpeed = mid
            else:
                minSpeed = mid + 1

        return minSpeed