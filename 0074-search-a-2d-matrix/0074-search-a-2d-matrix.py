class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n=len(matrix)
        m=len(matrix[0])
        i=0
        j=m-1
        while (i<n and j>=0):
            if matrix[i][j]==target:
                return True
            if matrix[i][j]>target:
                j-=1
            else:
                i+=1
        return False