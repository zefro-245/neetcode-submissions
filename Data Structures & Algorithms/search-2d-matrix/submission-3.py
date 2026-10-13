class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m*n - 1

        while left <= right:
            mid = left + (right-left)//2

            row = mid//n
            coloumn = mid%n

            if target == matrix[row][coloumn]:
                return True
            elif target<matrix[row][coloumn]:
                right=mid-1
            else:
                left=mid+1
        return False
        