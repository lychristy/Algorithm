#3 Sum 3 Arrays
class Solution(object):
  def exist(self, a, b, c, target):
    """
    input: int[] a, int[] b, int[] c, int target
    return: boolean
    """
    # write your solution here
    ht = {}

    for i in range(len(a)):
      ht[a[i]] = i

    for i in range(len(b)):
      for j in range(len(c)):
        if target - b[i] - c[j] in ht:
          return True
    return False
