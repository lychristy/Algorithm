#2 Sum
# return True or False. Determine if there exist two elements in a given array, the sum of which is the given target number.

class Solution(object):
  def existSum(self, array, target):
    """
    input: int[] array, int target
    return: boolean
    """
    # write your solution here

    ht = {}
    for i in range(len(array)):
      if array[i] in ht:
        return True
      else:
        ht[target - array[i]] = i
    return False