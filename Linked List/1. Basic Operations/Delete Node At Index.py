#Delete Node At Index
#Delete the node at the given index for the given linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
  def deleteNode(self, head, index):
    """
    input: ListNode head, int index
    return: ListNode
    """
    # write your solution here

    if head is None:
      return head
    
    p = ListNode(0)
    q = p
    i = 0

    while head is not None and i < index:
      p.next = head
      head = head.next
      p = p.next
      i += 1
    
    if i == index and head is not None:
      p.next = head.next
    
    return q.next