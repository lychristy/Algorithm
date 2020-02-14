#Search Common Element in Sorted Matrix
#Given a 2D integer matrix, where every row is sorted in ascending order. How to find a common element in all rows. If there is no common element, then returns -1.
class Solution(object):
  def search(self, matrix):
    """
    input: int[][] matrix
    return: int
    """
    # write your solution here
    if len(matrix) == 1:
      return -1
    
    row = len(matrix)
    ht = {}
    
    for i in range(row):
      col = len(matrix[i])
      
      for j in range(col):
        value = matrix[i][j]
        
        if j == 0:
          if value not in ht:
            ht[value] = 1
          else:
            ht[value] += 1
        elif value > matrix[i][j - 1]:
          if value not in ht:
            ht[value] = 1
          else:
            ht[value] += 1
    
    for ele in ht:
        if ht[ele] == row:
          return ele
    return -1

#Solution().search([[1,2,3,4,10,11,100,200],[5,6,7,8,9,10,10,11,100,101],[2,3,5,8,9,12,99,100]])