#Closest In Sorted Array
#Given a target integer T and an integer array A sorted in ascending order, find the index i in A such that A[i] is closest to T.

class Solution(object):
  def closest(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
    if array is None or len(array) is 0:
      return -1

    left = 0
    right = len(array) - 1

    while left < right - 1:
      mid = left + (right - left) // 2
      
      if array[mid] == target:
        return mid
      elif array[mid] > target:
        right = mid
      else:
        left = mid

    if abs(array[left] - target) <= abs(array[right] - target):
      return left
    
    return right