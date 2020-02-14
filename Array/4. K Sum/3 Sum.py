#3 Sum
#Determine if there exists three elements in a given array that sum to the given target number. Return all the triple of values that sums to target.

#Assumptions

#The given array is not null and has length of at least 3 
#No duplicate triples should be returned, order of the values in the tuple does not matter

#A = {1, 2, 2, 3, 2, 4}, target = 8, return [[1, 3, 4], [2, 2, 4]]

class Solution(object):
  def allTriples(self, array, target):
    """
    input: int[] array, int target
    return: int[][]
    """
    # write your solution here
    array.sort()
    res = []

    for k in reversed(range(2, len(array))):
      if k < len(array) - 1 and array[k] == array[k + 1]:
        continue
      
      i = 0
      j = k - 1

      while(i < j):
        if i > 0 and array[i] == array[i - 1]:
          i += 1
          continue
        
        sum = array[i] + array[j] + array[k]
        if sum == target:
          res.append([array[i], array[j], array[k]])
          i += 1
          j -= 1
        elif sum < target:
          i += 1
        else:
          j -= 1
    
    return res

Solution().allTriples([1,1,1,1,1,1,1,1,1,1,1],3)