#Spiral Order Generate II
#Generate an M * N 2D array in spiral order clock-wise starting from the top left corner, using the numbers of 1, 2, 3, …, M * N in increasing order.
class Solution(object):
  def spiralGenerate(self, m, n):
    """
    input: int m, int n
    return: int[][]
    """
    # write your solution here
    newList = list(range(1, m*n + 1))

    j = 0
    rowStart = 0
    colStart = 0
    rowEnd = m - 1
    colEnd = n - 1
    matrix = [row[:] for row in [[0]*n]*m]

    while rowStart <= rowEnd and colStart <= colEnd:
      for i in range(colStart, colEnd + 1):
        matrix[rowStart][i] = newList[j]
        j += 1
      for i in range(rowStart + 1, rowEnd + 1):
        matrix[i][colEnd] = newList[j]
        j += 1
      if rowStart < rowEnd:
        for i in reversed(range(colStart, colEnd)):
          matrix[rowEnd][i] = newList[j]
          j += 1
      if colStart < colEnd:
        for i in reversed(range(rowStart + 1, rowEnd)):
          matrix[i][colStart] = newList[j]
          j += 1
      rowStart += 1
      colStart += 1
      rowEnd -= 1
      colEnd -= 1
    return matrix