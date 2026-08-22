class Solution:
    def trap(self, height: List[int]) -> int:
        leftStack = []
        rightStack = []
        water = height.copy()
        for idx, hei in enumerate(height):
            if not leftStack or hei >= leftStack[-1][0]:
                if leftStack:
                    for i in range(leftStack[-1][1], idx):
                        water[i] = leftStack[-1][0]
                leftStack.append([hei, idx])
                

        for idx in range(len(height)-1, -1, -1):
            hei = height[idx]
            if not rightStack or hei >= rightStack[-1][0]:
                if rightStack:
                    for i in range(rightStack[-1][1], idx, -1):
                        water[i] = rightStack[-1][0]
                rightStack.append([hei, idx])
        
        for i in range(leftStack[-1][1], rightStack[-1][1]):
            water[i] = min(leftStack[-1][0], rightStack[-1][0])
        
        return sum(wat - hei for hei, wat in zip(height, water))



# [0,2,0,3,1,0,1,3,2,1]
# water -> max_k such that exist left and right having height at least k
# [0,2,2,3,3,3,3,3,2,1]

# return sum(height[i] - water[i])

# maxIndex: 
# record index that make new heightest (from start)
# same from the end