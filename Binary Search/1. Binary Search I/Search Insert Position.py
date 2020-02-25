#Search Insert Position
#Given a sorted array and a target value, return the index where it would be if it were inserted in order. 
#If there are multiple elements with value same as target, we should insert the target before the first existing element.

class Solution(object):
  def searchInsert(self, input, target):
    """
    input: int[] input, int target
    return: int
    """
    # write your solution here

    if len(input) is 0:
      return 0
    
    left = 0
    right = len(input) - 1

    while left < right - 1:
      mid = left + (right - left) // 2
      
      if input[mid] < target:
        left = mid + 1
      elif input[mid] > target:
        right = mid - 1
      else:
        right = mid
    
    if input[left] >= target:
      return left
    elif input[right] < target:
      return right + 1
    return right