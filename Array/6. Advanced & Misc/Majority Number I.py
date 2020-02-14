#Majority Number I

class Solution(object):
  def majority(self, array):
    """
    input: int[] array
    return: int
    """
    # write your solution here
    if len(array) == 1:
      return array[0]
      
    ht = {}  
    for i in range(len(array)):
      if array[i] not in ht:
        ht[array[i]] = 1
      else:
        ht[array[i]] += 1
    
    maxCount = 0
    majorityEle = []
    for ele in ht:
      if ht[ele] > maxCount:
        maxCount = ht[ele]
        majorityEle = ele
    
    return majorityEle