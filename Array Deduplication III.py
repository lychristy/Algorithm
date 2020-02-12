#Array Deduplication III
#{1, 2, 2, 3, 3, 3} → {1}
class Solution(object):
  def dedup(self, array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    if len(array) <= 1:
      return array
    
    dup = False
    j = 0

    for i in range(1, len(array)):
      if array[i] == array[j]:
        #duplicate
        dup = True
      elif dup is True:
        #previous is duplicate, now move new element, replace by the new element
        array[j] = array[i]
        dup = False
      else:
        #previous is not deplicate, keep the value and process the new element
        j += 1
        array[j] = array[i]

    if dup is True:
      return array[:j]
    else:
      return array[: (j+1)]

