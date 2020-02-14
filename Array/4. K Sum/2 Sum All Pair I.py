#2 Sum All Pair I
#find all paired indexes to the target sum

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
      if target - array[i] in ht:
        res.extend([j, i] for j in ht[target - array[i]])
      if array[i] in ht:
        ht[array[i]].append(i)
      else:
        ht[array[i]] = [i]
    
    return res