#Missing Number II
#Given an integer array of size N - 1 sorted by ascending order, containing all the numbers from 1 to N except one, find the missing number.
class Solution(object):
  def missing(self, array):
    """
    input: int[] array
    return: int
    """
    # write your solution here
    if len(array) is 0:
      return 1

    left = 0
    right = len(array) - 1

    while left < right:
      mid = left + (right - left) // 2

      if array[mid] - 2 == mid:
        right = mid
      else:
        left = mid + 1
    
    if array[right] - 2 == right:
      return right + 1
    
    return len(array) + 1