#Merge Two Sorted Array

#Input: [1, 2, 3], 3, [2, 4, 6], 1 
#Output: [1,2, 2, 3]

class Solution(object):
  def merge(self, A, m, B, n):
    """
    input: int[] A, int m, int[] B, int n
    return: int[]
    """
    # write your solution here
    array = []
    i = 0
    j = 0

    while i <= m - 1 or j <= n - 1:
      if i == m:
        array.append(B[j])
        j += 1
      elif j == n:
        array.append(A[i])
        i += 1
      else:
        if A[i] <= B[j]:
          array.append(A[i])
          i += 1
        else:
          array.append(B[j])
          j += 1
    return array
#Solution().merge([1,3,5,10,100,2000,-1,-1,-1,-1],6,[50,99,1999,5000],4)