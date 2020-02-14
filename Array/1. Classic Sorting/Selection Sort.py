#Selection Sort
#give array is null or length array is zero
class Solution(object):
  def solve(self, array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    if array is None or len(array) <= 1:
      return array

    for i in range(len(array)):
      minValue =  i

      j = i + 1
      while j <= len(array) - 1:
        if array[j] < array[minValue]:
          minValue = j
        j += 1
      array[i], array[minValue] = array[minValue], array[i]
    return array