class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = prices[0]
        total = 0

        for price in prices:
            if price > hold:
                total += price - hold
                hold = price
            else:
                hold = price
        
        return total