#2 Difference In Sorted Array
#Given a sorted array A, find a pair (i, j) such that A[j] - A[i] is identical to a target number(i != j).

#If there does not exist such pair, return a zero length array.

#Assumptions:
#The given array is not null and has length of at least 2.
#If more than one pair of index exits, return the one with ascending order.

class Solution(object):
  def twoDiff(self, array, target):
    """
    input: int[] array, int target
    return: int[]
    """
    # write your solution here
    if abs(array[len(array) - 1] - array[0]) < abs(target):
      return []
    
    res = []
    for i in range(len(array) - 1):
      for j in range(i + 1, len(array)):
        if array[j] - array[i] == target:
          return [i, j]
        elif array[j] - array[i] == -target:
          res = [j, i]
    
    return res