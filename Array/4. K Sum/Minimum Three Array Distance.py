#Minimum Three Array Distance
#Given three sorted integer arrays, pick one element from each of them, what is the min value of |x - y| + |y - z| + |z - x|.
class Solution(object):
  def minDistance(self, a, b, c):
    """
    input: int[] a, int[] b, int[] c
    return: int
    """
    # write your solution here
    minDis = abs(a[0] - b[0]) + abs(a[0] - c[0]) + abs(b[0] - c[0])
    for i in range(len(a)):
      for j in range(len(b)):
        for k in range(len(c)):
          dis = abs(a[i] - b[j]) + abs(a[i] - c[k]) + abs(b[j] - c[k])
          if minDis == 0:
            return 0
          if dis < minDis:
            minDis = dis
    return minDis
