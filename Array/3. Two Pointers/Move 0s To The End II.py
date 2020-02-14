#Move 0s To The End II
#The relative order of the elements in the original array need to be maintained.
class Solution(object):
  def moveZero(self, array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    if array is None or len(array) <= 1:
      return array
    
    index1 = 0
    index2 = 0

    while index2 <= len(array) - 1:
      if array[index2] is not 0:
        array[index1], array[index2] = array[index2], array[index1]
        index2 += 1
        index1 += 1
      else:
        index2 += 1
    return array
#Solution().moveZero([1, 0, 3, 0, 1])