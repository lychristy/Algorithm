#Majority Number III
#Given an integer array of length L, find all numbers that occur more than 1/K * L times if any exist.
class Solution(object):
  def majority(self, array, k):
    """
    input: int[] array, int k
    return: Integer[]
    """
    # write your solution here
    if len(array) == 0:
      return array
    
    ht = {}
    res = []

    for i in range(len(array)):
      if array[i] not in ht:
        ht[array[i]] = 1
      else:
        ht[array[i]] += 1

    for ele in ht:
      if ht[ele] * k > len(array):
        res.append(ele)
    
    return res