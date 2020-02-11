#Spiral Order Traverse II
#Traverse an M * N 2D array in spiral order clock-wise starting from the top left corner. Return the list of traversal sequence.
class Solution(object):
  def spiral(self, matrix):
    """
    input: int[][] matrix
    return: Integer[]
    """
    # write your solution here
    newList = []
    rowStart = 0
    colStart = 0
    rowEnd = len(matrix) - 1
    colEnd = len(matrix[0]) - 1

    while rowStart <= rowEnd and colStart <= colEnd:
      for i in range(colStart, colEnd + 1):
        newList.append(matrix[rowStart][i])
      for i in range(rowStart + 1, rowEnd + 1):
        newList.append(matrix[i][colEnd])
      if rowStart < rowEnd:
        for i in reversed(range(colStart, colEnd)):
          newList.append(matrix[rowEnd][i])
      if colStart < colEnd:
        for i in reversed(range(rowStart + 1, rowEnd)):
          newList.append(matrix[i][colStart])
      rowStart += 1
      colStart += 1
      rowEnd -= 1
      colEnd -= 1
    return newList

#a = [[1, 2, 3, 4], [5, 6, 7, 8],  [13, 14, 15, 16]]
#a = [[1,2,3,4,5],[6,7,8,9,10]]
#a = [[1]]
#Solution().spiral(a)
