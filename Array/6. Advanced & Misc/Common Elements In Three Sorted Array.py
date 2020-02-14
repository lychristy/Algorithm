#Common Elements In Three Sorted Array

#Find all common elements in 3 sorted arrays. A = {1, 2, 2, 3}, B = {2, 2, 3, 5}, C = {2, 2, 4}, the common elements are [2, 2]
class Solution(object):
  def common(self, a, b, c):
    """
    input: int[] a, int[] b, int[] c
    return: Integer[]
    """
    # write your solution here
    res = []

    i = 0
    j = 0
    k = 0

    while i < len(a) and j < len(b) and k < len(c):
      if a[i] == b[j] == c[k]:
        res.append(a[i])
        i += 1
        j += 1
        k += 1
      elif a[i] <= b[j] and a[i] <= c[k]:
        i += 1
      elif b[j] <= a[i] and b[j] <= c[k]:
        j += 1
      else:
        k += 1
    return res