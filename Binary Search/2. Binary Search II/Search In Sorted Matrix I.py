#Search In Sorted Matrix I
#Given a target number, returning the position that the target locates within the matrix. If the target number does not exist in the matrix, return {-1, -1}.

class Solution(object):
  def search(self, matrix, target):
    """
    input: int[][] matrix, int target
    return: int[]
    """
    # write your solution here
    N = len(matrix)
    M = len(matrix[0])

    left = 0
    right = N * M - 1

    while left <= right:
      mid = left + (right - left) // 2
      
      row = mid // M
      col = mid % M
      value = matrix[row][col]

      if value == target:
        return [row, col]
      elif value < target:
        left = mid + 1
      else:
        right = mid - 1
    
    return [-1, -1]

Solution().search([[1, 2, 3, 4]], 4)