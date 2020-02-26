#Delete Nodes At Indices
#1 -> 2 -> 3 -> 4 -> NULL, indices = {0, 3, 5}, after deletion the list is 2 -> 3 -> NULL.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
  def deleteNodes(self, head, indices):
    """
    input: ListNode head, int[] indices
    return: ListNode
    """
    # write your solution here
    if head is None:
      return head

    p = ListNode(0)
    q = p

    i = 0
    j = 0
    while head is not None and j < len(indices):
      if i == indices[j]:
        j += 1
      else:
        p.next = head
        p = p.next
      i += 1
      head = head.next
    
    p.next = head
    
    return q.next