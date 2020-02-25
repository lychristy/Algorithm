#Classical Binary Search

class Solution(object):
  def binarySearch(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
    if array is None or len(array) == 0:
      return -1
    
    left = 0
    right = len(array) - 1
    while left <= right:
      mid = left + (right - left) // 2
      if array[mid] == target:
        return mid
      elif array[mid] < target:
        left = mid + 1
      else:
        right = mid - 1
    
    return -1