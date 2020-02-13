#3Sum Smaller
class Solution(object):
  def threeSumSmaller(self, num, target):
    """
    input: int[] num, int target
    return: int
    """
    # write your solution here
    num.sort()
    count = 0

    for k in reversed(range(2, len(num))):
      i = 0
      j = k - 1

      while i < j:
        sum = num[i] + num[j] + num[k]
        if sum < target:
          count += j - i
          i += 1
        else:
          j -= 1
    
    return count