#Move 0s To The End I
#The relative order of the elements in the original array does not need to be maintained.
class Solution(object):
  def moveZero(self, array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    if array is None or len(array) <= 1:
      return array
    
    left = 0
    right = len(array) - 1

    while left <= right:
      if array[left] is not 0:
        left += 1
      elif array[right] is 0:
        right -= 1
      else:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    return array
