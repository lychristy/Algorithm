#Set Matrix Zeroes
#Given a m x n matrix, if an element is 0, set its entire row and column to 0.
class Solution(object):
  def setZero(self, matrix):
    """
    input: int[][] matrix
    return: No need to return
    """
    # write your solution here
    if matrix is None or len(matrix) < 1:
      return matrix
      
    rowNum = len(matrix) - 1
    colNum = len(matrix[0]) - 1
    row = [False for i in range(rowNum + 1)]
    col = [False for i in range(colNum + 1)]

    for i in range(rowNum + 1):
      for j in range(colNum + 1):
        if matrix[i][j] == 0:
          row[i] = True
          col[j] = True
    
    for i in range(rowNum + 1):
      for j in range(colNum + 1):
        if row[i] is True or col[j] is True:
          matrix[i][j] = 0
    return matrix


#Solution().setZero([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
#Solution().setZero([])