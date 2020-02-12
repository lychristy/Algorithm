#Interleave Positive And Negative Elements
#{1, 2, 3, 4, 5, -1, -1, -1} --> {1, -1, 2, -1, 3, -1, 4, 5}  (The ordering of positive/negative numbers do not matter)
class Solution(object):
  def interleave(self, array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here

    if len(array) <= 1:
      return array
    
    left = 0
    right = len(array) - 1

    while left <= right:
      if array[left] > 0:
        left += 1
      else:
        array[left], array[right] = array[right], array[left]
        right -= 1
    
    left = 1
    right = right + 1
    
    while left <= right - 1 and right < len(array):
      array[left], array[right] = array[right], array[left]
      left += 2
      right += 1
    
    return array

#Solution().interleave([1, -1, 1, -1, 1])