#Rainbow Sort II
#sort the balls : Red, Green, Blue or Black,  (0, 1, 2, 3)
class Solution(object):
  def rainbowSortII(self, array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    if len(array) <= 1:
      return array
    
    zero = 0
    one = 0
    two = len(array) - 1
    three = len(array) - 1

    while one <= two:
      if array[one] is 0:
        array[zero], array[one] = array[one], array[zero]
        zero += 1
        one += 1
      elif array[one] is 1:
        one += 1
      elif array[two] is 3:
        array[two], array[three] = array[three], array[two]
        two -= 1
        three -= 1
      elif array[two] is 2:
        two -= 1
      else:
        array[two], array[one] = array[one], array[two]
    
    return array