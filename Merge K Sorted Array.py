#Merge K Sorted Array
#Merge K sorted array into one big sorted array in ascending order. The input arrayOfArrays is not null, none of the arrays is null either

class Solution(object):
  def merge(self, arrayOfArrays):
    """
    input: int[][] arrayOfArrays
    return: int[]
    """
    # write your solution here
    k = len(arrayOfArrays)

    if k == 1:
      return arrayOfArrays[0]
    
    res = arrayOfArrays[0]
    
    for i in range(1, k):
      j = 0
      k = 0
      tempArray = arrayOfArrays[i]
      tempRes = []

      while j < len(res) or k < len(tempArray):
        if j == len(res):
          tempRes.append(tempArray[k])
          k += 1
        elif k == len(tempArray):
          tempRes.append(res[j])
          j += 1
        else:
          if res[j] <= tempArray[k]:
            tempRes.append(res[j])
            j += 1
          else:
            tempRes.append(tempArray[k])
            k += 1
      res = tempRes
    
    return res
#Solution().merge([[3],[1,2,3,4,5]])