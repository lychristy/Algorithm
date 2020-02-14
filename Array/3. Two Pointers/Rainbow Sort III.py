#Rainbow Sort III
#Given an array of balls with k different colors denoted by numbers 1- k, sort the balls.
class Solution(object):
  def rainbowSortIII(self, array, k):
    """
    input: int[] array, int k
    return: int[]
    """
    # write your solution here
    if len(array) <= 1 or k == 1:
      return array
    
    self.rainbowSort(array, 0, len(array) - 1, k)
    return array

  def rainbowSort(self, array, left, right, k):
    if k == 1:
      return
    if left >= right:
      return
    pivot = self.partition(array, left, right, k)
    k -= 1
    self.rainbowSort(array, left, pivot, k)
  
  def partition(self, array, left, right, k):
    while left <= right:
      if array[left] == k:
        array[left], array[right] = array[right], array[left]
        right -= 1
      else:
        left += 1
    return right

#Solution().rainbowSortIII([1,3,4,2,5,5,4,2,1],5)