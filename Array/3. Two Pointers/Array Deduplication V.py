#Array Deduplication V
#Given an integer array(not guaranteed to be sorted), remove adjacent repeated elements.For each group of elements with the same value keep at most two of them. {2, 1, 2, 2, 2, 3} --> {2, 1, 2, 2, 3}  
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
      if array[i] is not array[j - 2] or array[i] is not array[j - 1]:
        array[j] = array[i]
        j += 1
    return array[:j]

#Solution().dedup([4, 4, 4, 1, 2, 3, 3, 3])