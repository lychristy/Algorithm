#Different Elements In Two Sorted Arrays

#a = {1, 2, 2, 3, 4, 5} b = {2, 2, 2, 4, 4, 6}

#The returned two lists are: [[1, 3, 5],[2, 4, 6]]  // there are two 2s in a, so there is one 2 in b not in a

class Solution(object):
  def diff(self, a, b):
    """
    input: int[] a, int[] b
    return: int[][]
    """
    # write your solution here
    i = 0
    lefti = 0
    j = 0
    leftj = 0

    while i < len(a) and j < len(b):
      if a[i] < b[j]:
        a[lefti] = a[i]
        i += 1
        lefti += 1
      elif a[i] == b[j]:
        i += 1
        j += 1
      else:
        b[leftj] = b[j]
        j += 1
        leftj += 1
      
    if i == len(a):
      while j < len(b):
        b[leftj] = b[j]
        leftj += 1
        j += 1
    while i < len(a):
      a[lefti] = a[i]
      lefti += 1
      i += 1
    
    return [a[:lefti], b[:leftj]]
#Solution().diff([1, 2, 2, 3, 4, 5], [2, 2, 2, 4, 4, 6])