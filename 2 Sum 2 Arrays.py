#2 Sum 2 Arrays
#Given two arrays A and B, determine whether or not there exists a pair of elements, one drawn from each array, that sums to the given target number.

class Solution(object):
  def existSum(self, a, b, target):
    """
    input: int[] a, int[] b, int target
    return: boolean
    """
    # write your solution here
    ht = {}

    for i in range(len(a)):
      ht[a[i]] = i
    
    for i in range(len(b)):
      if target - b[i] in ht:
        return True
    
    return False
