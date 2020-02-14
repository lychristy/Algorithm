#Number Of Negative Numbers In Sorted Matrix

#More Optimal Solution: m*logn, binary search
class Solution(object):
  def negNumber(self, matrix):
    """
    input: int[][] matrix
    return: int
    """
    # write your solution here
    count = 0
    row = len(matrix)
    for i in range(row):
      col = len(matrix[i])
      for j in range(col):
        if matrix[i][j] < 0:
          count += 1
    return count