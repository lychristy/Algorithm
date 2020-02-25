#Square Root I
#Given an integer number n, find its integer square root. 
#Input: 18, Return: 4 Input: 4, Return: 2

class Solution(object):
  def sqrt(self, x):
    """
    input: int x
    return: int
    """
    # write your solution here
    if x < 2:
      return x

    left = 1
    right = x

    while left < right - 1:
      mid = left + (right - left) // 2
      if x / mid == mid:
        return mid
      elif x / mid < mid:
        right = mid - 1
      else:
        left = mid
      
    if x / right > right:
      return right
    
    return left
    
Solution().sqrt(5)