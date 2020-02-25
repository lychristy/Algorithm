#Shift Position
#Given an integer array A, A is sorted in ascending order first then shifted by an arbitrary number of positions, For Example, A = {3, 4, 5, 1, 2} (shifted left by 2 positions). Find the index of the smallest number.
class Solution(object):
  def shiftPosition(self, array):
    """
    input: int[] array
    return: int
    """
    # write your solution here

    if array is None or len(array) is 0:
      return -1
    if len(array) is 1:
      return 0
    
    left = 0
    right = len(array) - 1

    while left <= right:
      mid = left + (right - left) // 2

      if array[left] <= array[mid] and array[mid] <= array[right]:
        right = mid - 1
      elif array[mid] >= array[left]:
        left = mid + 1
      else:
        right = mid
    return left


Solution().shiftPosition([2,1])