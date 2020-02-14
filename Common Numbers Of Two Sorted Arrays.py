#Common Numbers Of Two Sorted Arrays

#Find all numbers that appear in both of two sorted arrays (the two arrays are all sorted in ascending order). Both two arrays are not null.
#A = {1, 1, 2, 2, 3}, B = {1, 1, 2, 5, 6}, common numbers are [1, 1, 2]

class Solution(object):
  def common(self, A, B):
    """
    input: Integer[] A, Integer[] B
    return: Integer[]
    """
    # write your solution here
    i = 0
    j = 0
    lefti = 0

    while i < len(A) and j < len(B):
      if A[i] < B[j]:
        i += 1
      elif A[i] > B[j]:
        j += 1
      else:
        A[lefti], A[i] = A[i], A[lefti]
        i += 1
        lefti += 1
        j += 1
        
    return A[:lefti]
#Solution().common([1,1,2,3],[1,1,1,1,1,1,1,1,1,2,3])