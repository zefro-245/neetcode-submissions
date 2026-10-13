class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        right=len(matrix)-1
        

        while left <= right:
            mid = left + (right-left)//2
            if target==matrix[mid][0]:
                return True
            elif target>matrix[mid][0]:
                left = mid+1
            elif target<matrix[mid][0]:
                right = mid-1
 
        if right < 0:
            return False

        row = right

        left2 = 0
        right2 = len(matrix[0])-1
        while left2<=right2:
            mid2 = left2 + (right2-left2)//2
            if target==matrix[row][mid2]:
                return True
            if target>matrix[row][mid2]:
                left2=mid2+1
            else:
                right2=mid2-1
        return False
