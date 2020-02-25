#Search In Sorted Matrix II

#Given a 2D matrix that contains integers only, which each row is sorted in ascending order and each column is also sorted in ascending order.
#Given a target number, returning the position that the target locates within the matrix. If the target number does not exist in the matrix, return {-1, -1}.

class Solution(object):
  def search(self, matrix, target):
    """
    input: int[][] matrix, int target
    return: int[]
    """
    # write your solution here

    if matrix is None or len(matrix) is 0 or len(matrix[0]) is 0:
      return [-1, -1]

    row = len(matrix)
    col = len(matrix[0])

    i = 0
    j = col - 1

    while i < row and j >= 0:
      value = matrix[i][j]
      
      if value == target:
        return [i, j]
      elif value < target:
        i += 1
      else:
        j -= 1
    
    return [-1, -1]