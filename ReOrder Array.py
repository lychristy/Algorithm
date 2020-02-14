#ReOrder Array

#Given an array of elements, reorder it as follow:
#{ N1, N2, N3, …, N2k } → { N1, Nk+1, N2, Nk+2, N3, Nk+3, … , Nk, N2k }
#{ N1, N2, N3, …, N2k+1 } → { N1, Nk+1, N2, Nk+2, N3, Nk+3, … , Nk, N2k, N2k+1 }

class Solution(object):
  def reorder(self, array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here

    if len(array) <= 3:
      return array

    mid = len(array) // 2 - 1
    res = []

    for i in range(mid + 1):
      j = i + mid + 1
      res.append(array[i])
      res.append(array[j])

    if len(array) % 2 == 1:
      res.append(array[j + 1])
    return res   