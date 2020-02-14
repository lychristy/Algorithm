#Array Deduplication I
#Given a sorted integer array, remove duplicate elements.
class Solution(object):
  def dedup(self, array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    if len(array) <= 1:
      return array
    
    j = 1

    for i in range(1, len(array)):
      if array[i] > array[j - 1]:
        array[j] = array[i]
        j += 1
    return array[:j]

#Solution().dedup([1,2,3,4,4,5])