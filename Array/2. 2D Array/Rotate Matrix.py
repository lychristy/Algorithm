#Rotate Matrix
#Rotate an N * N matrix clockwise 90 degrees.
class Solution(object):
  def rotate(self, matrix):
    """
    input: int[][] matrix
    return: No need to return
    """
    # write your solution here
    if len(matrix) <= 1:
      return matrix
    n = (len(matrix) + 1 ) // 2

    right = len(matrix) - 1
    level = len(matrix)
    for left in range(n + 1):
      for i in range(level - 1):
        temp = matrix[left][left + i]
        matrix[left][left + i] = matrix[right - i][left]
        matrix[right - i][left] = matrix[right][right - i]
        matrix[right][right - i] = matrix[left + i][right]
        matrix[left + i][right] = temp
      right -= 1
      level -= 2

    return matrix

#Solution().rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])