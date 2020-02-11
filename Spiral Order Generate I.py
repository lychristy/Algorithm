#Spiral Order Generate I
#Generate an N * N 2D array in spiral order clock-wise starting from the top left corner, using the numbers of 1, 2, 3, …, N * N in increasing order.
class Solution(object):
  def spiralGenerate(self, n):
    """
    input: int n
    return: int[][]
    """
    # write your solution here
    newList = list(range(1, n*n + 1))

    j = 0
    start = 0
    end = n - 1
    matrix = [row[:] for row in [[0]*n]*n]

    while start < end:
      for i in range(start, end + 1):
        matrix[start][i] = newList[j]
        j += 1
      for i in range(start + 1, end + 1):
        matrix[i][end] = newList[j]
        j += 1
      for i in reversed(range(start, end)):
        matrix[end][i] = newList[j]
        j += 1
      for i in reversed(range(start + 1, end)):
        matrix[i][start] = newList[j]
        j += 1
      start += 1
      end -= 1
    
    if start == end :
      matrix[start][end] = newList[j]
    
    return matrix
#Solution().spiralGenerate(3)
