#Insertion Sort
#given array is null or array length is zero

class Solution(object):
  def sort(self, array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    if array is None or len(array) <= 1:
      return array

    for i in range(1, len(array)):

      key = array[i]
      j = i - 1
      while array[j] > key and j >= 0:
        array[j + 1] = array[j]
        j -= 1
      array[j + 1] = key 
    return array