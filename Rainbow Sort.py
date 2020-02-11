#Rainbow Sort
#3 classes: -1, 0, 1
class Solution(object):
  def rainbowSort(self, array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    if array is None or len(array) <= 1:
      return array

    neg = 0
    zero = 0
    one = len(array) - 1

    while(zero <= one):
      if array[zero] is 1:
        array[zero], array[one] = array[one], array[zero]
        one -= 1
      elif array[zero] is -1:
        array[zero], array[neg] = array[neg], array[zero]
        zero += 1
        neg += 1
      else:
        zero += 1
    return array