#Sum All Pair II
#Return all the distinct pairs of values.

class Solution(object):
  def allPairs(self, array, target):
    """
    input: int[] array, int target
    return: int[][]
    """
    # write your solution here
    ht = {}
    res = []

    for i in range(len(array)):
      if target - array[i] in ht and ht[target - array[i]] == 0:
        res.append([array[i], target - array[i]])
        ht[array[i]] = 1
        ht[target - array[i]] = 1
      elif target - array[i] not in ht:
        ht[array[i]] = 0
      else:
        ht[array[i]] = 1
    
    return res
