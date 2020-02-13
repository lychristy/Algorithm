#4 Sum
#Determine if there exists a set of four elements in a given array that sum to the given target number.
class Solution(object):
  def exist(self, array, target):
    """
    input: int[] array, int target
    return: boolean
    """
    # write your solution here
    ht = {}

    for i in range(len(array) - 1):
      level = {}
      for j in range(i + 1, len(array)):
        sum = array[i] + array[j]
        
        if target - sum in ht and ht[target - sum] is not j and ht[target - sum] is not i:
          return True
        
        level[sum] = j
      
      ht.update(level)
    return False

#Solution().exist([3, 1, 6, 2, 5, 9, 4], 9)
#Solution().exist([3, 1, 6, 3, 16, 40], 23)