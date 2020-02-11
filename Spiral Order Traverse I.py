#Spiral Order Traverse I
#Traverse an N * N 2D array in spiral order clock-wise starting from the top left corner. Return the list of traversal sequence.
"""
Created on Mon Feb 10 16:01:33 2020

@author: yliu
"""
class Solution(object):
  def spiral(self, matrix):
    """
    input: int[][] matrix
    return: Integer[]
    """
    # write your solution here
    newList = []
    start = 0
    end = len(matrix) - 1
    
    while start < end:
      for i in range(start, end + 1):
        newList.append(matrix[start][i])
        
      for i in range(start + 1, end + 1):
        newList.append(matrix[i][end] )
        
      for i in reversed(range(start, end)):
        newList.append(matrix[end][i])
        
      for i in reversed(range(start + 1, end)):
        newList.append(matrix[i][start])
        
      start += 1
      end -= 1
    if start == end:
      newList.append(matrix[start][end])
    return newList


#a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

#Solution().spiral(a)