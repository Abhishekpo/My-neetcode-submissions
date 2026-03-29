class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row=len(matrix)
        col=len(matrix[0])
        def binarySearch(i, L, R):
            while L<=R:
        
             mid=(R+L)//2
             if matrix[i][mid]==target:
                 return True
             elif matrix[i][mid] > target:
                 R =mid-1
             else:
                 L =mid+1

        for i in range(row):
            if binarySearch(i, 0, col-1):
                return True

        return False

            