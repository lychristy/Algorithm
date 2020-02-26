#Linked List Insert At Index
#1 -> 2 -> 3 -> null, insert 4 at index 3, --> 1 -> 2 -> 3 -> 4 -> null
#1 -> 2 -> null, insert 4 at index 0, --> 4 -> 1 -> 2 -> null

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
  def insert(self, head, index, value):
    """
    input: ListNode head, int index, int value
    return: ListNode
    """
    
    p = ListNode(0)
    p.next = head
    q = p
    i = 0
    
    while i < index and p.next is not None:
      p = p.next
      i += 1
    
    if i == index:
      next = p.next
      p.next = ListNode(value)
      p.next.next = next
    
    return q.next