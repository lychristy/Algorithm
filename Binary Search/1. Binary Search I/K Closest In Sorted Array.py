#K Closest In Sorted Array
#Given a target integer T, a non-negative integer K and an integer array A sorted in ascending order, find the K closest numbers to T in A.
#A = {1, 4, 6, 8}, T = 3, K = 3, return {4, 1, 6}
class Solution(object):
  def kClosest(self, array, target, k):
    """
    input: int[] array, int target, int k
    return: int[]
    """
    # write your solution here

    left = 0
    right = len(array) - 1

    while left < right - 1:
      mid = left + (right - left) // 2

      if array[mid] == target:
        right = mid
      elif array[mid] < target:
        left = mid
      else:
        right = mid
    
    res = []
    for i in range(1, k + 1):
      if left < 0:
        res.append(array[right])
        right += 1
      elif right >= len(array):
        res.append(array[left])
        left -= 1
      else:
        if abs(array[left] - target) <= abs(array[right] - target):
          res.append(array[left])
          left -= 1
        else:
          res.append(array[right])
          right += 1
    return res