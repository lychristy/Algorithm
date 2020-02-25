#Search In Shifted Sorted Array I
#Given a target integer T and an integer array A, A is sorted in ascending order first, then shifted by an arbitrary number of positions.

#For Example, A = {3, 4, 5, 1, 2} (shifted left by 2 positions). Find the index i such that A[i] == T or return -1 if there is no such index.
#A = {3, 4, 5, 1, 2}, T = 4, return 1
class Solution(object):
  def search(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
    if array is None or len(array) is 0:
      return -1
    
    left = 0
    right = len(array) - 1

    while left <= right:
      mid = left + (right - left) // 2
      if array[mid] == target:
        return mid
      
      if array[mid] < array[right]:
        if array[mid] < target and target <= array[right]:
          left = mid + 1
        else:
          right = mid - 1
      else:
        if array[left] <= target and target < array[mid]:
          right = mid - 1
        else:
          left = mid + 1
    return -1
Solution().search([20, 30, 2, 12, 13, 14, 15], 30)