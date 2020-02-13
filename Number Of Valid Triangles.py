#Number Of Valid Triangles
#Given an unsorted array of positive integers. Find the number of triangles that can be formed with three different array elements as three sides of triangles.
class Solution(object):
  def numOfTriangles(self, array):
    """
    input: int[] array
    return: int
    """
    # write your solution here
    count = 0
    array.sort()

    for i in range(len(array) - 2):
      k = i + 2
      for j in range(i + 1, len(array) - 1):
        while k < len(array) and array[i] + array[j] > array[k]:
          k += 1
        count += k - j - 1

    return count