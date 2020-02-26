#Remove Linked List Elements
#Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
  def removeElements(self, head, val):
    """
    input: ListNode head, int val
    return: ListNode
    """
    # write your solution here
    if head is None:
      return head

    p = ListNode(0)
    q = p

    while head is not None:
      if head.val is not val:
        q.next = head
        q = q.next
      head = head.next
    q.next = None
    
    return p.next