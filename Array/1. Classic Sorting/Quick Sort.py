#Quick Sort
#give array is null or length array is zero

class Solution(object):
  def quickSort(self, array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    if array is None or len(array) <= 1:
      return array

    self.quickSort1(array, 0, len(array) - 1)
    return array

  def quickSort1(self, array, left, right):
    if left >= right:
      return
    pivot = self.partition(array, left, right)
    self.quickSort1(array, left, pivot - 1)
    self.quickSort1(array, pivot + 1, right)
    
  def partition(self, array, left, right):
    pivot = right
    leftBound = left
    rightBound = right - 1

    while leftBound <= rightBound:
      if array[leftBound] <= array[pivot]:
        leftBound += 1
      elif array[rightBound] > array[pivot]:
        rightBound -= 1
      else:
        array[rightBound], array[leftBound] = array[leftBound], array[rightBound]
        leftBound += 1
        rightBound -= 1
    array[pivot], array[leftBound] = array[leftBound], array[pivot]
    return leftBound

#Solution().quickSort([4, 2, 1, 6, 3, 5])