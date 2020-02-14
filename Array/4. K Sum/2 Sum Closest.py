#2 Sum Closest
#Find the pair of elements in a given array that sum to a value that is closest to the given target number. A = {1, 4, 7, 13}, target = 7, closest pair is 1 + 7 = 8, return [1, 7].
class Solution(object):
  def closest(self, array, target):
    """
    input: int[] array, int target
    return: Integer[]
    """
    # write your solution here
    array.sort()
    left = 0
    right = len(array) - 1
    minValue = abs(target - (array[left] + array[right]))

    res = [array[left], array[right]]
    
    while left < right:
      diff = abs(target - (array[left] + array[right]))
      if diff < minValue:
        minValue = diff
        res = [array[left], array[right]]
        
      if minValue == 0:
        return [array[left], array[right]]
      elif array[left] + array[right] > target:
        right -= 1
      else:
        left += 1
    
    return res