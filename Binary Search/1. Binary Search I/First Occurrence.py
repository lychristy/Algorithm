#First Occurrence
#Given a target integer T and an integer array A sorted in ascending order, find the index of the first occurrence of T in A or return -1 if there is no such index.
class Solution(object):
  def firstOccur(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here

    if array is None or len(array) is 0:
      return -1

    left = 0
    right = len(array) - 1

    while left < right:
      mid = left + (right - left) // 2
      if array[mid] >= target:
        right = mid
      else:
        left = mid + 1
    
    if array[left] == target:
      return left
    
    return -1