#Merge Sort
class Solution(object):
  def mergeSort(self, array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    if array is None or len(array) <= 1:
      return array

    self.mergeSort1(array, 0, len(array) - 1)
    return array

  def mergeSort1(self, array, left, right):
    if left >= right:
      return
    mid = int(left + (right - left) / 2)
    self.mergeSort1(array, left, mid)
    self.mergeSort1(array, mid + 1, right)
    self.merge(array, left, mid, right)
    
  def merge(self, array, left, mid, right):
    helper = array.copy()
    leftIndex = left
    rightIndex = mid + 1

    while leftIndex <= mid and rightIndex <= right:
      if helper[leftIndex] <= helper[rightIndex]:
        array[left] = helper[leftIndex]
        left += 1
        leftIndex += 1
      else:
        array[left] = helper[rightIndex]
        left += 1
        rightIndex += 1
      
    while leftIndex <= mid:
      array[left] = helper[leftIndex]
      left += 1
      leftIndex += 1
        
#Solution().mergeSort([4, 2, 1, 6, 3, 5])