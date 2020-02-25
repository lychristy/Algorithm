#Find Local Minimum
#Given an unsorted integer array, return any of the local minimum's index.An element at index i is defined as local minimum when it is smaller than all its possible two neighbors a[i - 1] and a[i + 1]
#(you can think a[-1] = +infinite, and a[a.length] = +infinite)

class Solution(object):
  def localMinimum(self, array):
    """
    input: int[] array
    return: int
    """
    # write your solution here
    if len(array) is 1:
      return 0

    left = 0
    right = len(array) - 1

    while left <= right:
      mid = left + (right - left) // 2
      
      prev = array[mid] + 1 if mid == 0 else array[mid - 1]
      next = array[mid] + 1 if mid == len(array) - 1 else array[mid + 1]
      
      if array[mid] < prev and array[mid] < next:
        return mid
      elif prev < array[mid]:
        right = mid - 1
      else:
        left = mid + 1
    
    return -1