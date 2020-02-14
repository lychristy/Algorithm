#3Sum Closest
class Solution(object):
  def threeSumClosest(self, num, target):
    """
    input: int[] num, int target
    return: int
    """
    # write your solution here
    num.sort()
    min = abs(num[0] + num[len(num) - 1] + num[len(num) - 2] - target)

    for k in reversed(range(2, len(num))):
      i = 0
      j = k -1

      while i < j:
        sum = num[i] + num[j] + num[k]
        diff = abs(sum - target)
        if diff < min:
          min = diff
        
        if sum == target:
          return 0
        elif sum < target:
          i += 1
        else:
          j -= 1
    
    return min
Solution().threeSumClosest([9, -1, 3, 13, 10, 17, 7, 3], 50)