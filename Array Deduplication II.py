#Array Deduplication II
#Given a sorted integer array, remove duplicate elements.  At most 2 same values
class Solution(object):
  def dedup(self, array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    if len(array) <= 2:
      return array
    
    j = 2
    for i in range(2, len(array)):
      if array[i] > array[j - 2]:
        array[j] = array[i]
        j += 1
    
    return array[:j]
#Solution().dedup([1,1,1])