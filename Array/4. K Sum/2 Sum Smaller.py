#2 Sum Smaller
#Determine the number of pairs of elements in a given array that sum to a value smaller than the given target number.
class Solution(object):
  def smallerPairs(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
    array.sort()

    left = 0
    right = len(array) - 1
    count = 0

    while left < right:
      sum = array[left] + array[right]
      if sum < target:
        count += right - left
        left += 1
      else:
        right -= 1
    return count