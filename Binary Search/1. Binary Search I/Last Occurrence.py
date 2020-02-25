#Last Occurrence
#Given a target integer T and an integer array A sorted in ascending order, find the index of the last occurrence of T in A or return -1 if there is no such index.
class Solution(object):
  def lastOccur(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here

    if array is None or len(array) is 0:
      return -1

    left = 0
    right = len(array) - 1

    while left < right - 1:
      mid = left + (right - left) // 2

      if array[mid] > target:
        right = mid - 1
      else:
        left = mid

    if array[right] == target:
      return right
    elif array[left] == target:
      return left
    return -1
Solution().lastOccur([1, 2, 2, 2, 3], 2)