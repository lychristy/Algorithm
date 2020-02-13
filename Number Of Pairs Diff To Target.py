#Number Of Pairs Diff To Target
class Solution(object):
  def pairs(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
    ht = {}
    count = 0
    
    for i in range(len(array)):
      if target + array[i] in ht:
        count += ht[target + array[i]]
      if array[i] - target in ht:
        count += ht[array[i] - target]
      
      if array[i] not in ht:
        ht[array[i]] = 1
      else:
        ht[array[i]] += 1
    
    return count