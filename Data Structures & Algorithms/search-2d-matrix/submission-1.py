class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        maxRow = len(matrix)
        maxCol = len(matrix[0])

        low = 0
        high = maxRow * maxCol

        

        while low < high:
            index = (low + high)//2
            val = matrix[index // maxCol][index % maxCol]
            if val == target:
                return True
            elif low + 1 == high:
                break
            elif val < target:
                low = index
            else:
                high = index


        return False