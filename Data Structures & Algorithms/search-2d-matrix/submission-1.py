class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        left = 0
        right = n * m - 1

        while left <= right:
            middle = int(left + (right - left)/2)

            i = int(middle / m) 
            j = int(middle % m)

            if matrix[i][j] == target: 
                return True
        
            if matrix[i][j] < target:
                left = middle + 1
        
            else: 
                right = middle - 1
    
        return False



        