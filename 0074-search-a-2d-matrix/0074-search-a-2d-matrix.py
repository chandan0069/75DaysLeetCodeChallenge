class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n=len(matrix)
        m=len(matrix[0])
        low=0
        high=(n*m)-1
        while low<=high:
            mid = (low+(high-low)/2)
            if matrix[mid/m][mid%m]==target:
                return True
            if matrix[mid/m][mid%m]>target:
                high=mid-1
            else:
                low=mid+1
        return False